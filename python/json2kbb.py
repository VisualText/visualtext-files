# DESC: Build KBB files from any .json files in kb/user/ (json -> knowledge base)
#
# WHAT IT DOES
#   Scans the analyzer's kb/user/ directory for "*.json" files and, for every
#   "<name>.json" that does NOT already have a matching "<name>.kbb", converts
#   the JSON into a KBB knowledge-base file "<name>.kbb" in the same directory.
#   The engine then loads that .kbb into the KB like any other kbb file.
#
# HOW TO USE
#   1. Put your data file "<name>.json" in the analyzer's  kb/user/  folder.
#   2. Add this script to the analyzer sequence as a python pass placed BEFORE
#      the tokenizer:  Sequence view -> right-click the tokenizer (or a pass) ->
#      "Insert Python Library Pass (Before Tokenizer)" -> choose "json2kbb".
#   3. Run the analyzer. On each run this pass builds any missing "<name>.kbb"
#      from "<name>.json" before the KB is loaded, so the data is available to
#      later passes.
#   To REBUILD after editing a .json, delete its "<name>.kbb" and run again
#   (an existing .kbb is left untouched so hand-edited KBs are never clobbered).
#
#   The engine invokes a python pass as:
#       python "<appdir>/spec/json2kbb.py" "<appdir>" "<inputfile>" <pre|post>
#   Only <appdir> is used (to locate kb/user/); the input file is ignored.
#
# JSON -> KBB MAPPING  (the inverse of KBFuncs.nlp's JsonKB serializer)
#   - a JSON object            -> a concept
#   - "key": <primitive>       -> an attribute on the concept:  key=value
#   - "key": { object }        -> a child concept:  key:
#   - "key": [ array ]         -> counted child concepts:  key1:, key2:, ...
#                                 (each element's members become its attrs/children;
#                                  a primitive element becomes  keyN: value=<primitive>)
#   KBB text format (see the engine's parseKBBLine): 2 spaces per indent level,
#   "name:" optionally followed by comma-separated "attr=value" pairs; children
#   are indented +2. Values are bare when simple tokens, else double-quoted.
#
#   Example:  { "company": { "name": "Acme Corp", "founded": 1990,
#                 "dept": [ {"name":"Eng"}, {"name":"Sales"} ] } }
#   becomes:
#       company: name="Acme Corp", founded=1990
#         dept1: name=Eng
#         dept2: name=Sales
#
# Any failure (bad/unreadable JSON) is non-fatal: a warning is printed to stderr
# and the analyzer pipeline continues.

import sys
import os
import io
import json

INDENT = "  "  # 2 spaces per level; the engine reads indent/2 as the depth


def is_primitive(v):
    return not isinstance(v, (dict, list))


def is_simple_token(s):
    # bare (unquoted) when it is a simple identifier-ish token; else quote it
    return len(s) > 0 and all(c.isalnum() or c in "_-." for c in s)


def format_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if is_simple_token(s):
        return s
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + s + '"'


def split_members(obj):
    # attributes = primitive members; children = object/array members
    attrs, children = [], []
    for key, val in obj.items():
        if val is None:
            continue
        if isinstance(val, (dict, list)):
            children.append((key, val))
        else:
            attrs.append((key, val))
    return attrs, children


def write_concept_line(out, level, name, attrs):
    line = INDENT * level + str(name) + ":"
    if attrs:
        line += " " + ", ".join(k + "=" + format_value(v) for k, v in attrs)
    out.write(line + "\n")


def write_object(out, level, name, obj):
    attrs, children = split_members(obj)
    write_concept_line(out, level, name, attrs)
    write_children(out, level + 1, children)


def write_children(out, level, children):
    for key, val in children:
        if isinstance(val, dict):
            write_object(out, level, key, val)
        elif isinstance(val, list):
            for i, element in enumerate(val, start=1):
                cname = str(key) + str(i)
                if isinstance(element, dict):
                    write_object(out, level, cname, element)
                elif isinstance(element, list):
                    write_concept_line(out, level, cname, [])
                    write_children(out, level + 1, [("item", element)])
                else:
                    write_concept_line(out, level, cname, [("value", element)])


def json_to_kbb(data, root_name):
    out = io.StringIO()
    if isinstance(data, dict) and len(data) == 1 and isinstance(next(iter(data.values())), dict):
        # single object root: use the top-level key as the root concept
        (key, value), = data.items()
        write_object(out, 0, key, value)
    elif isinstance(data, dict):
        write_object(out, 0, root_name, data)
    else:
        # top-level array or primitive: wrap under a root concept named for the file
        if is_primitive(data):
            write_concept_line(out, 0, root_name, [("value", data)])
        else:
            write_concept_line(out, 0, root_name, [])
            write_children(out, 1, [("item", data)])
    return out.getvalue()


def convert_file(jsonpath, kbbpath):
    with open(jsonpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    stem = os.path.splitext(os.path.basename(jsonpath))[0]
    kbb = json_to_kbb(data, stem)
    with open(kbbpath, "w", encoding="utf-8") as f:
        f.write(kbb)


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("[json2kbb: usage: json2kbb.py <appdir> [<inputfile>] [pre|post]]\n")
        return
    appdir = sys.argv[1]
    kbdir = os.path.join(appdir, "kb", "user")
    if not os.path.isdir(kbdir):
        sys.stderr.write("[json2kbb: no kb/user directory at " + kbdir + "]\n")
        return

    made = 0
    for name in sorted(os.listdir(kbdir)):
        if not name.lower().endswith(".json"):
            continue
        stem = os.path.splitext(name)[0]
        kbbpath = os.path.join(kbdir, stem + ".kbb")
        if os.path.exists(kbbpath):
            continue  # already built; delete the .kbb to regenerate
        jsonpath = os.path.join(kbdir, name)
        try:
            convert_file(jsonpath, kbbpath)
            made += 1
            sys.stderr.write("[json2kbb: built " + kbbpath + "]\n")
        except Exception as e:
            sys.stderr.write("[json2kbb: failed on " + jsonpath + ": " + str(e) + "]\n")

    if made == 0:
        sys.stderr.write("[json2kbb: no new .json files to convert in " + kbdir + "]\n")


if __name__ == "__main__":
    main()
