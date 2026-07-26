# 📢 Announcement — See Your Parse Tree

![NLP++ parse-tree graphic](ParseTreeGraphic.png)

**Every `.tree` file your analyzer writes can now be drawn as a classic linguistic tree
diagram** — right inside VS Code, beside the text file it came from.

NLP++ has always given you the parse tree as text: one indented line per node, with its
span and type. That's precise, and it's still there. But a tree is a *picture*, and now you
can see it as one — phrases branching over their words, exactly the way a linguist would
draw it on a whiteboard.

---

## Opening the graphic

From any `.tree` file:

- 🌲 **The tree button** in the editor title bar — draws the whole tree.
- 🖱️ **Right-click → Graph Entire Tree** — the same thing, from the context menu.
- 🖱️ **Right-click → Graph Selected Portion of Tree** — draws just the **selected lines**,
  or, with nothing selected, the **subtree under your cursor**. Perfect for looking at one
  noun phrase in a 400-node tree.

The graphic is strictly on-demand: opening a `.tree` file never draws anything on its own,
so tree files still open instantly. And it re-uses a single panel, so asking for another
tree replaces the one you're looking at instead of piling up tabs.

---

## Getting around the tree

The whole diagram is live. The hint bar along the bottom sums it up, but here it is in full:

| Do this | Get this |
| --- | --- |
| **Scroll** | Zoom in and out |
| **Shift + scroll** | Squeeze or spread the horizontal spacing between nodes |
| **Drag** | Pan around the canvas |
| **Click a phrase node** | Open **one level** — just that node's children |
| **Click a word (leaf)** | **Reveal it in the text** — selects that word in the input file |
| **Right-click** | Menu (below) |

Trees open with the root expanded and everything else closed, so you **drill down one node
at a time** rather than being hit with hundreds of tokens at once. Small trees (roughly 30
nodes or fewer) open fully, and every tree is fit to the window when it opens.

Labels don't collide, either: at **every level** of the tree, labels that would overlap are
staggered into the minimum number of extra rows needed — and they drop back onto a single
line as soon as they fit, or as soon as you spread the tree out with Shift + scroll.

---

## The right-click menu

Right-click anywhere in the graphic:

- **Reveal Text** — on **any** node, word or phrase. Selects that node's whole span in the
  analyzed text file. Right-click an `_np` and the entire noun phrase lights up.
- **Expand all below** / **Collapse all below** — open or close an entire subtree at once
  (shown on nodes that have children).
- **Center all** — fit the whole tree back into the window.
- **Expand all** / **Collapse all** — open or close the entire tree.

---

## The text `.tree` file still does everything it did

The graphic is an *alternative* view, not a replacement. In the `.tree` file itself, put
your cursor on **any node line** and right-click:

- **Highlight text** — selects that node's text in the input file and opens it beside the
  tree. Works on any node, at any depth — click a phrase node and you highlight the whole
  phrase; click a word and you highlight the word.
- **Display Rule Fired** — opens the pass that built the node and jumps straight to the rule
  that fired (for nodes that came from a dictionary, it searches the dictionaries instead).
- **Generate @PATH** — writes the context `@PATH` for that node, ready to paste into a rule.
- **Open Pass File** — jumps to the pass that produced this tree.
- **Fold / Unfold** (all, or recursively) — collapse the text tree the same way you collapse
  the graphic.

Between the two views you get both halves of the picture: the graphic for *shape* — how the
parse actually came together — and the text file for *detail*, the spans, the rules, and the
paths you need when you sit down to write the next rule.

**Read the full guide:** [Parse Trees](../parsetrees.md)

_See more on the [Help home](../home.md)._
