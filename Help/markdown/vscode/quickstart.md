# Quick Start

[← Back to Help home](home.md)

This page gets you from zero to writing your own analyzers.

## 1. Install the NLP++ extension

In VS Code, open the **Extensions** view (`Ctrl+Shift+X`) and search for **`nlp`** — the
**NLP++** extension is at the top of the results. Click **Install**.

The first time it runs, it offers to download the **NLP engine** and its VisualText
support files — accept that so analyzers can run.

## 2. Load the example analyzers

In the **Analyzers** view, click the little **⚙️ cog (gear) icon** — *Load Example Analyzers*.

- **VS Code reloads.** After it reopens, **open the bottom panel and click *VisualText* again**.
- You'll now see the **tutorial** analyzers and the **NLPFix** analyzers in the Analyzers view.

## 3. Run and play with the examples

1. Click different analyzers in the **Analyzers** view to load them.
2. Choose a text file in the **Text** view.
3. Click the **▶ run** button to analyze that text.

Output appears in the **Output Files** and **Logging** views; the parse tree and any
`output.json` land under the text file's `_log/` folder. Open passes in the **Analyzer**
(sequence) view to see how each one works.

> ⚠️ **Copy them out before you change them.** If you want to keep your edits, right-click
> → **Copy All Analyzers to Another Folder** and work on the copy. The originals are
> **overwritten on the next automatic update** of the VisualText files.

## 4. Create your own analyzer

In the **Analyzers** view, click the **New Analyzer** icon and choose a **template**. Your
new analyzer is created with the standard `spec/ input/ kb/` layout, ready for you to add
text files and write passes.

## 5. Use Claude to help you write an analyzer

You can use **Claude** (Anthropic's AI coding assistant) right inside VS Code to help you
build your analyzer:

1. Install the **Claude Code** extension from the Extensions view.
2. Sign in to link it to your Claude subscription — the extension walks you through this.
3. [**Click here to create a Claude prompt**](command:helpView.createClaudePrompt) (or click **Create Claude Prompt** in the NLP++ **Help** panel). It opens a new editor with a ready-to-paste prompt — already filled in with your machine's engine, example/template analyzer, and library paths. Copy that prompt into Claude to get started.

## More help

- **[Compiling Analyzers](compiling.md)** — make runs fast and distribute analyzers without source.
- **[Regression Testing](testing.md)** — lock in your analyzer's output with golden files.
