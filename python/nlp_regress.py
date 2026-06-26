#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nlp_regress.py - golden-file regression tester for NLP++ analyzers.

It runs every file under an analyzer's ``input/`` directory through the NLP++
engine, captures the structured extraction (the ``output.json`` the analyzer
emits), and compares it against a committed *golden* copy under
``<analyzer>/test/expected/``.

WHY A SEMANTIC COMPARE (and not a byte diff):
    The engine's raw output drifts across versions (per-rule provenance
    comments, extra diagnostic prints, renumbered ``id`` fields). A byte/text
    diff therefore breaks on cosmetic engine changes - which is exactly why the
    NLPPlus package's own fixture tests are currently skipped. This tool
    compares the *set of extracted records* with the volatile ``id`` field
    removed, so it is stable across cosmetic engine changes yet still catches a
    real regression: an added, removed, or changed extraction.

ENGINE BACKENDS (auto-detected, in priority order):
    1. The ``NLPPlus`` Python package (``pip install NLPPlus``) - cross-platform,
       no engine path needed. Used by CI.
    2. The ``nlp`` / ``nlp.exe`` command-line engine - for local dev against the
       VS Code "VisualText" extension's bundled engine. The engine working
       directory is found from ``--engine``, ``$NLP_ENGINE``, or auto-detection.

COMMANDS:
    bless   run every input and (over)write the goldens under test/expected/
    test    run every input, compare to goldens, print a diff, exit non-zero on
            any regression
    list    show the discovered input files and whether each has a golden

USAGE:
    python nlp_regress.py test  path/to/analyzer
    python nlp_regress.py bless path/to/analyzer
    python nlp_regress.py test  path/to/analyzer --engine /path/to/nlp-engine
    python nlp_regress.py test  ./telephone ./emailaddress   # several at once

Pure Python 3 standard library; runs on Windows, macOS and Linux.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Config / discovery
# ---------------------------------------------------------------------------

# Files under input/ that are documentation or engine artefacts, not test
# inputs. (Per-analyzer overrides live in test/regress.json -> "exclude".)
DEFAULT_EXCLUDE_NAMES = {"SOURCES.md", "README.md", "sources.md", "readme.md"}
DEFAULT_EXCLUDE_SUFFIXES = {".json"}
# A directory the engine writes next to each input ("<file>_log/"); never an input.
LOG_DIR_SUFFIX = "_log"

# Record fields dropped before comparison (volatile / non-semantic).
DEFAULT_IGNORE_FIELDS = ("id",)


def load_config(analyzer_dir):
    """Optional per-analyzer config at <analyzer>/test/regress.json."""
    cfg_path = analyzer_dir / "test" / "regress.json"
    cfg = {
        "exclude": [],          # extra glob patterns (relative to input/) to skip
        "include": [],          # if set, ONLY these globs are tested
        "ignore_fields": list(DEFAULT_IGNORE_FIELDS),
    }
    if cfg_path.is_file():
        try:
            cfg.update(json.loads(cfg_path.read_text(encoding="utf-8")))
        except Exception as exc:  # noqa: BLE001
            warn(f"could not read {cfg_path}: {exc}")
    return cfg


def find_inputs(analyzer_dir, cfg):
    """Every regular file under <analyzer>/input/ that is a test input."""
    input_root = analyzer_dir / "input"
    if not input_root.is_dir():
        return []
    inputs = []
    for path in sorted(input_root.rglob("*")):
        if not path.is_file():
            continue
        # skip anything inside an engine "<file>_log" output directory
        if any(part.endswith(LOG_DIR_SUFFIX) for part in path.relative_to(input_root).parts):
            continue
        if path.name in DEFAULT_EXCLUDE_NAMES:
            continue
        if path.suffix.lower() in DEFAULT_EXCLUDE_SUFFIXES:
            continue
        rel = path.relative_to(input_root)
        if cfg.get("include"):
            if not any(rel.match(g) for g in cfg["include"]):
                continue
        if any(rel.match(g) for g in cfg.get("exclude", [])):
            continue
        inputs.append(path)
    return inputs


def golden_path(analyzer_dir, input_path):
    """Where the golden for an input lives, mirroring the input/ tree."""
    rel = input_path.relative_to(analyzer_dir / "input")
    return analyzer_dir / "test" / "expected" / (str(rel) + ".json")


# ---------------------------------------------------------------------------
# Normalization (semantic comparison)
# ---------------------------------------------------------------------------

def canon(obj, ignore_fields):
    """
    Canonicalize an output object for stable comparison:
      - drop volatile fields (``id`` ...) from every dict, recursively;
      - sort any list whose items are dicts (extraction records) so that a
        renumber / reorder is not flagged as a regression.
    """
    if isinstance(obj, dict):
        return {k: canon(v, ignore_fields) for k, v in obj.items()
                if k not in ignore_fields}
    if isinstance(obj, list):
        items = [canon(v, ignore_fields) for v in obj]
        if items and all(isinstance(v, (dict, list)) for v in items):
            items.sort(key=lambda v: json.dumps(v, sort_keys=True, ensure_ascii=False))
        return items
    return obj


def records(obj):
    """Flatten the extraction records (leaf list-of-dicts) for a readable diff."""
    out = []
    if isinstance(obj, dict):
        for v in obj.values():
            out.extend(records(v))
    elif isinstance(obj, list):
        if obj and all(isinstance(v, dict) for v in obj):
            out.extend(obj)
        else:
            for v in obj:
                out.extend(records(v))
    return out


def diff_records(expected, actual, ignore_fields):
    """Return (removed, added) lists of records (as compact dicts)."""
    def bag(o):
        b = {}
        for r in records(o):
            key = json.dumps({k: v for k, v in r.items() if k not in ignore_fields},
                             sort_keys=True, ensure_ascii=False)
            b[key] = b.get(key, 0) + 1
        return b
    eb, ab = bag(expected), bag(actual)
    removed = [k for k, n in eb.items() for _ in range(max(0, n - ab.get(k, 0)))]
    added = [k for k, n in ab.items() for _ in range(max(0, n - eb.get(k, 0)))]
    return removed, added


# ---------------------------------------------------------------------------
# Engine backends
# ---------------------------------------------------------------------------

class NlpPlusBackend:
    """Run analyzers through the cross-platform NLPPlus Python package."""

    name = "NLPPlus"

    def __init__(self):
        import NLPPlus  # noqa: F401  (import error -> backend unavailable)
        self._nlp = NLPPlus

    def analyze(self, analyzer_dir, input_path):
        analyzer_dir = Path(analyzer_dir).resolve()
        # NLPPlus resolves an analyzer by NAME inside a working folder that
        # contains it; point the working folder at the analyzer's parent.
        self._nlp.set_working_folder(str(analyzer_dir.parent))
        text = read_text(input_path)
        result = self._nlp.engine.analyze(text, analyzer_dir.name)
        out = getattr(result, "output", None)
        if isinstance(out, str):
            out = json.loads(out) if out.strip() else {}
        return out or {}


class CliBackend:
    """Run analyzers through the nlp / nlp.exe command-line engine."""

    name = "nlp CLI"

    def __init__(self, engine_dir, binary):
        self.engine_dir = Path(engine_dir)
        self.binary = binary

    def analyze(self, analyzer_dir, input_path):
        analyzer_dir = Path(analyzer_dir).resolve()
        input_path = Path(input_path).resolve()
        log_dir = Path(str(input_path) + LOG_DIR_SUFFIX)
        if log_dir.exists():            # JsonKB appends; start clean
            shutil.rmtree(log_dir, ignore_errors=True)
        cmd = [str(self.binary), "-ANA", str(analyzer_dir),
               "-WORK", str(self.engine_dir), str(input_path)]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                       check=False)
        out_json = log_dir / "output.json"
        try:
            data = json.loads(out_json.read_text(encoding="utf-8")) if out_json.is_file() else {}
        finally:
            shutil.rmtree(log_dir, ignore_errors=True)
        return data or {}


def detect_cli_engine(explicit):
    """Find an nlp-engine working dir + the nlp binary, or return (None, None)."""
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    for env in ("NLP_ENGINE", "NLPPLUS_WORK", "NLPENGINE"):
        if os.environ.get(env):
            candidates.append(Path(os.environ[env]))
    # common VS Code "VisualText" extension install locations
    home = Path.home()
    for ext_root in (home / ".vscode" / "extensions",
                     home / ".vscode-server" / "extensions",
                     home / ".vscode-insiders" / "extensions"):
        if ext_root.is_dir():
            candidates += sorted(ext_root.glob("dehilster.nlp-*/nlp-engine"))
    binname = "nlp.exe" if os.name == "nt" else "nlp"
    for cand in candidates:
        if not cand or not cand.is_dir():
            continue
        local = cand / binname
        if local.exists():
            return cand, local
        found = shutil.which(binname)
        if found:                       # engine dir given, binary on PATH
            return cand, Path(found)
    return None, None


def make_backend(args):
    """Pick the engine backend: NLPPlus unless --cli or import fails."""
    if not args.cli:
        try:
            return NlpPlusBackend()
        except Exception:               # noqa: BLE001  (package not installed)
            pass
    engine_dir, binary = detect_cli_engine(args.engine)
    if not engine_dir:
        die("no engine found. Install the NLPPlus package (pip install NLPPlus) "
            "or pass --engine <nlp-engine-dir> (or set $NLP_ENGINE).")
    info(f"engine: {binary}")
    return CliBackend(engine_dir, binary)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_bless(analyzer_dir, backend, cfg):
    inputs = find_inputs(analyzer_dir, cfg)
    if not inputs:
        warn(f"{analyzer_dir.name}: no input files found under input/")
        return 0
    n = 0
    for inp in inputs:
        out = backend.analyze(analyzer_dir, inp)
        gp = golden_path(analyzer_dir, inp)
        gp.parent.mkdir(parents=True, exist_ok=True)
        gp.write_text(json.dumps(canon(out, cfg["ignore_fields"]),
                                 indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                      encoding="utf-8")
        n += 1
    info(f"{analyzer_dir.name}: blessed {n} golden(s) under test/expected/")
    return 0


def cmd_test(analyzer_dir, backend, cfg):
    inputs = find_inputs(analyzer_dir, cfg)
    if not inputs:
        warn(f"{analyzer_dir.name}: no input files found under input/")
        return 0
    ignore = cfg["ignore_fields"]
    passed = failed = missing = 0
    for inp in inputs:
        rel = inp.relative_to(analyzer_dir / "input")
        gp = golden_path(analyzer_dir, inp)
        actual = canon(backend.analyze(analyzer_dir, inp), ignore)
        if not gp.is_file():
            missing += 1
            print(f"  MISSING  {rel}  (no golden - run 'bless')")
            continue
        expected = json.loads(gp.read_text(encoding="utf-8"))
        if expected == actual:
            passed += 1
            continue
        failed += 1
        print(f"  FAIL     {rel}")
        removed, added = diff_records(expected, actual, ignore)
        for r in removed:
            print(f"      - {r}")
        for a in added:
            print(f"      + {a}")
        if not removed and not added:   # structural change with no record delta
            print("      (output structure changed; see test/expected/ vs run)")
    total = passed + failed + missing
    status = "OK" if (failed == 0 and missing == 0) else "REGRESSION"
    print(f"  {analyzer_dir.name}: {passed}/{total} passed"
          + (f", {failed} failed" if failed else "")
          + (f", {missing} missing" if missing else "")
          + f"   [{status}]")
    return 1 if (failed or missing) else 0


def cmd_list(analyzer_dir, backend, cfg):
    inputs = find_inputs(analyzer_dir, cfg)
    print(f"{analyzer_dir.name}: {len(inputs)} input file(s)")
    for inp in inputs:
        rel = inp.relative_to(analyzer_dir / "input")
        have = "golden" if golden_path(analyzer_dir, inp).is_file() else "  -   "
        print(f"  [{have}] {rel}")
    return 0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_text(path):
    return Path(path).read_text(encoding="utf-8", errors="replace")


def info(msg):
    print(msg)


def warn(msg):
    print(f"warning: {msg}", file=sys.stderr)


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def resolve_analyzers(paths):
    """Accept analyzer dirs; an input/ child marks a valid analyzer."""
    out = []
    for p in paths:
        d = Path(p).resolve()
        if (d / "input").is_dir() and (d / "spec").is_dir():
            out.append(d)
        else:
            warn(f"skipping {p}: not an analyzer (needs input/ and spec/)")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Golden-file regression tester for NLP++ analyzers.")
    ap.add_argument("command", choices=("test", "bless", "list"))
    ap.add_argument("analyzers", nargs="+",
                    help="one or more analyzer directories (each with input/ + spec/)")
    ap.add_argument("--engine", help="nlp-engine working directory (CLI backend)")
    ap.add_argument("--cli", action="store_true",
                    help="force the nlp CLI backend instead of the NLPPlus package")
    args = ap.parse_args(argv)

    analyzers = resolve_analyzers(args.analyzers)
    if not analyzers:
        die("no valid analyzer directories given.")

    # 'list' needs no engine; 'test'/'bless' do.
    backend = None if args.command == "list" else make_backend(args)
    info(f"backend: {backend.name if backend else 'n/a'}")

    rc = 0
    for analyzer_dir in analyzers:
        cfg = load_config(analyzer_dir)
        fn = {"test": cmd_test, "bless": cmd_bless, "list": cmd_list}[args.command]
        rc |= fn(analyzer_dir, backend, cfg)
    return rc


if __name__ == "__main__":
    sys.exit(main())
