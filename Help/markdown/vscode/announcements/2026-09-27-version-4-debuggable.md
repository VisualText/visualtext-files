# 📢 Announcement — Version 4: NLP++ Is Debuggable

**You can now stop an analyzer in the middle of a run and look at it.** Set a breakpoint on a
rule, press Debug, and the engine halts on that rule — at the node it is being tried against,
with the text it is matching, the nodes it is about to take, and every variable in scope.

Glass-box NLP has always meant you could read the rules and audit the result. What you could
not do was watch the decision being made: the only window into a run was a `.tree` dump read
afterwards, from which you inferred backwards. **The glass box now has a door.**

---

## What you can do while it's stopped

- 🔴 **Break anywhere.** On a rule — clicking any element line snaps to the rule head the
  engine reports — and inside `@CODE`, `@POST` and `@DECL`, where the line you clicked *is*
  the unit that runs, so the stop happens before that line acts.
- 👣 **Step at the right granularity.** The three buttons mean one thing at a rule and the
  usual thing inside a statement body:

  | | at a rule | in a statement body |
  | --- | --- | --- |
  | **Step Over** | next rule tried | next statement, calls run whole |
  | **Step Into** | next rule matched | next statement, entering a call |
  | **Step Out** | next pass | until this function returns |

- 🔍 **Read your variables.** `L()` locals, `S()` suggested, `X()` context and `N()` matched
  elements, with `G()` globals in their own scope. The `N()` rows are labelled `N(1)`, `N(2)`
  — the expression you would actually write, not a description of it.
- 🎯 **See the nodes in play.** Not the whole tree from `_ROOT`, but the handful of nodes the
  rule is about: at a match, exactly what it took; at an attempt, the current node and the
  candidates after it as `+1`, `+2`, `+3`. When fewer nodes remain than the rule has elements,
  the pane says so instead of looking truncated.
- 🪜 **Follow the call stack.** A frame per call, each named for its function and opening on
  the line the call was *written* on, down to the `@POST` that started it.
- ⏪ **Or step backwards.** Replay mode walks the parse trees a finished run left on disk, so
  moving backward through a whole analysis costs nothing. Pass-level, and reversible.

---

## Getting in

**You do not need a `launch.json`.** Pick a text file in the **Text** view, press
**Debug Analyzer on Current File** on that view's toolbar, and the analyzer, the text file,
the engine and the port are filled in from what you have selected. F5 works the same way with
no configuration at all.

Three routes exist when you want them — `NLP++: debug (live)`, `NLP++: debug (replay)` and
`NLP++: attach (live)`, the last for an engine already running under
`nlp -ANA ... -DEBUG <port>`.

---

## NLP++ now runs outside VS Code, too

Every language feature — outline, hover, go-to-definition, references, rename, completion,
signature help, folding, semantic highlighting, quick fixes, diagnostics and formatting — now
runs in a **language server**. Nothing changed for VS Code, but the same answers are available
to any LSP editor, and as of 4.2.0 to a **web page**: the server also builds for a Web Worker,
with the page sending the analyzer's files in place of a disk.

---

Version 3 was about how you **build, deploy and install** an analyzer — compiled analyzers,
cloud builds, npm and pip. Version 4 is about how you **develop and understand** one.

**Read the full summary:** [Version 4 — NLP++ Is Debuggable](../versions/4.0.0.md)

_See more on the [Help home](../home.md)._
