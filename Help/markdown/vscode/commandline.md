# Command Line

`nlp.exe` (`nlp` on Linux and macOS) runs an analyzer from a terminal, a script or
CI. VS Code runs it for you; this page is for running it yourself. `nlp --help`
prints the same list.

[← Back to Help home](home.md)

## Usage

```
nlp -ANA <analyzer> [-WORK <engine folder>] [options] <input> [<outdir>]
nlp -ANA <analyzer> [-WORK <engine folder>] [options] -STDIN
nlp --help | --version
```

A typical run, from anywhere:

```
nlp -ANA C:\analyzers\myanalyzer -WORK C:\nlp-engine C:\analyzers\myanalyzer\input\text.txt
```

Switches are not case-sensitive (`-dev` is `-DEV`). An unknown switch, or a switch
missing its value, stops the run with a message and exit status 1.

## Running

| Switch | What it does |
|---|---|
| `-ANA analyzer` | The analyzer folder: a path, or a name under `<engine folder>/analyzers`. Required. |
| `-WORK folder` | The **engine folder**, the one holding `data/` and `analyzers/`. Default: the current folder. Point it at the analyzer folder instead and the engine prints "ERROR IN ANALYZER INIT" and runs only the tokenizer. |
| `-IN input` | The input file, or a folder of them (a folder run). Or give it as the first plain argument. |
| `-OUT folder` | The folder for this run's logs and trees, in place of `<input>_log`; made if missing (engine 4.2.51). Or give it as the second plain argument. |
| `-STDIN` | Load the analyzer once, then analyze one input file path per line of standard input; a blank line or the end of input ends the run. See [$isdirrun](../$isdirrun.md). |
| `-DATUM value` | A string the analyzer reads as [`G("$datum")`](../$datum.md), such as the output format the caller wants. |

Each input's logs and trees go in `<input>_log` next to the input, or in the
`-OUT` folder. Files the analyzer writes itself (`"out.txt" << ...`) go there too.

## Debugging

| Switch | What it does |
|---|---|
| `-DEV` | Write logs and the parse tree after every pass, as `ana001.tree`, `ana002.tree` and so on. Slow on large inputs: about 3.6 times as long on parse-en-us. The analyzer can test it with [`$dev`](../$dev.md). |
| `-SILENT` | Write no logs or output files, not even the analyzer's own. See [`$silent`](../$silent.md). |
| `-DEBUG port` | Wait for a rule debugger on `127.0.0.1:port`, then run under it; VS Code attaches this way. See [Version 4: debuggable](announcements/2026-09-27-version-4-debuggable.md). |
| `-DICTSOURCE` | Nodes built from `.dict` entries get `dictfile` and `dictline` attributes naming the entry's file and line. See [The analyzer sequence](../VisualText_Basics/About_the_analyzer_sequence.md). |

## Limits and zone mode

| Switch | What it does |
|---|---|
| `-TIMELIMIT seconds` | Stop an input's analysis that runs longer, at its next while turn or pass; the run then exits 2. |
| `-ZONES 40-45` | Zone mode: run only these zones. A zone (`7`), a range (`40-45`) or a list (`3,40-45`), counted from 1 as in the `z040-ana###.tree` names; the other zones get only the passes before the `zone` line (engine 4.2.50). See [Large Files](largefiles.md). |

## Compiled analyzers

| Switch | What it does |
|---|---|
| `-COMPILE` | Generate C++ for the analyzer and its knowledge base. Does not analyze. |
| `-COMPILEKB` | Generate C++ for the knowledge base only. |
| `-COMPILEANA` | Generate C++ for the analyzer only. |
| `-COMPILED` | Run the compiled analyzer (the `bin/run` and `bin/kb` libraries) instead of its `.nlp` files. |
| `-INTERP` | Run the analyzer from its `.nlp` files. The default. |

See [Compiling Analyzers](compiling.md) for building the libraries.

## Other

| Switch | What it does |
|---|---|
| `--help` | Print the switches and exit. |
| `--version` | Print the engine version, such as `4.2.51`, and exit. |

## Environment

| Variable | What it does |
|---|---|
| `NLP_REC_LIMIT=N` | A region of a `rec` pass may match N times plus N/50 per node before it is stopped; N is 1000 by default, and 0 lifts the limit. See [Large Files](largefiles.md#safety-limits). |

## Exit status

| Status | Meaning |
|---|---|
| 0 | Success. |
| 1 | Bad arguments, or a missing analyzer, input or output folder. Before engine 4.2.51 a missing input file exited 0. |
| 2 | A run stopped at `-TIMELIMIT`. |

The largest input the engine accepts is 2,000,000,000 bytes; a larger one is
refused with a message.

## Examples

Debug one input:

```
nlp -ANA myanalyzer -WORK C:\nlp-engine -DEV input\text.txt
```

Analyze every file of a folder, loading the analyzer once:

```
nlp -ANA myanalyzer -WORK C:\nlp-engine input
```

Stream a list of files, in order:

```
dir /b /s C:\corpus\*.txt | nlp -ANA myanalyzer -WORK C:\nlp-engine -STDIN
find corpus -name '*.txt' | sort | nlp -ANA myanalyzer -WORK ~/nlp-engine -STDIN
```

Ask for JSON, and give up after a minute:

```
nlp -ANA myanalyzer -WORK C:\nlp-engine -DATUM json -TIMELIMIT 60 input\text.txt
```

Rerun zones 40 to 45 of a large document with full trees, into a folder of their own:

```
nlp -ANA parse-en-us -WORK C:\nlp-engine -ZONES 40-45 -DEV -OUT C:\debug\z40 book.txt
```

From Python or Node.js, the same engine runs through the `NLPPlus` and `nlpplus`
packages; see [Calling Analyzers from Python & Node.js](packages.md).

## See also

[Large Files](largefiles.md) &nbsp;|&nbsp;
[Compiling Analyzers](compiling.md) &nbsp;|&nbsp;
[Special variables](../NLP_PP_Stuff/Special_Variables.md) &nbsp;|&nbsp;
[Calling Analyzers from Python & Node.js](packages.md)
