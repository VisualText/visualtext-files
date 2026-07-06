# Compiling Analyzers

By default the extension runs an analyzer **interpreted** from its NLP++ source. You can
also **compile** it into native libraries — for faster runs and to share an analyzer
without exposing its source. Everything here is done from the extension's UI; you never
touch a command line.

[← Back to Help home](home.md)

## The three kinds of compile

| Command | What it compiles | Library produced |
|---|---|---|
| **Compile Analyzer and KB** | the rules **and** the knowledge base together | `<analyzerName>.dll` |
| **Compile Analyzer Only** | just the rules (reuses the already-built KB) | `analyzer.dll` |
| **Compile KB** | just the knowledge base | `kb.dll` |

(`.dll` on Windows, `.so` on Linux, `.dylib` on macOS.)

**Where the menu items are:** in the **Analyzers** view —

- **Right-click an analyzer** → the three compile commands are in the menu, **or**
- open the Analyzers view's **`⋯` (More Actions)** / title menu, where the same commands live.

Use **Compile Analyzer Only** for fast turnaround when you've changed only rules; use
**Compile KB** when only the knowledge base changed; use **Compile Analyzer and KB** to
build everything (for example before distributing).

## Watching it compile — the status bar

When a compile starts, progress is shown in the **status bar** (for example
*"Compile Analyzer and KB…"*). A local build can take a little while; a cloud build may
wait for a build runner, so the status-bar progress is the place to watch.

- On success a notification reports the library it produced (with **Reveal in Explorer**).
- On failure, open the **NLP++ output / Logging** panel for details.

## Where the library files appear

After a successful compile, the library files — `kb.dll`, `analyzer.dll`, and/or
`<analyzerName>.dll` — show up in the **KB view**, listed alongside the knowledge-base
sources. (All three can coexist, one per compile kind.)

## Running a compiled version — the Run-mode toggle

The **status bar** has a **Run-mode** item. Click it to cycle through the modes:

**Interpreted → Compiled KB → Compiled Analyzer → Compiled → (back to Interpreted)**

| Run mode | What runs |
|---|---|
| **Run: Interpreted** | the NLP++ source (default) |
| **Run: Compiled KB** | compiled `kb.dll`; the analyzer rules stay interpreted |
| **Run: Compiled Analyzer** | compiled `analyzer.dll`; the KB stays interpreted |
| **Run: Compiled** | both compiled together (`<analyzerName>.dll`) |

The status bar always shows the current mode. Then just run your analyzer the usual way
(the ▶ run button). If you pick a compiled mode but haven't built that library yet, the
extension tells you and offers to compile it (or to switch back to **Interpreted**).

## Tip

After compiling, use **[Regression Testing](testing.md)** to confirm the compiled
analyzer produces the same output as the interpreted one.