[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# callanalyzer

## Purpose

Run another analyzer's passes on part of the current parse tree, using the current knowledge base.

## Syntax

```
returnedBool = callanalyzer(pnode, concept, analyzerStr)
```

```
returnedBool - type: bool (1,0)

pnode - type: pnode

concept - type: concept

analyzerStr - type: str
```

## Returns

1 if the analyzer ran, else 0. When it returns 0, the reason is written to the calling analyzer's `err.log`.

## Remarks

`callanalyzer` lets you build one analyzer out of several separately written analyzers, all working on the same parse tree and the same knowledge base. For example, an analyzer that finds addresses can hand each address node to an address analyzer, and an analyzer that finds sentences can hand each sentence node to a parser.

**What the called analyzer works on.** The called analyzer has no text or parse tree of its own. Its passes run on the subtree under `pnode`: its rules match `pnode`'s children the way an analyzer's rules normally match the children of the root, and `pnroot()` returns `pnode`. It changes the caller's tree directly, so any nodes it builds, renames or gives variables are still there when the call returns. It also uses the caller's knowledge base, and [callconcept](callconcept.md) returns `concept`, the concept it was given for its results. Anything it adds under that concept is in the caller's knowledge base immediately.

**What is loaded once.** The first call builds the called analyzer's passes and reads its `kb/user` dictionary (`.dict`) and `.kbb` files into the knowledge base. Its lazily loaded `*full.dict` and `*full.kbb` files are registered with the knowledge base rather than read. The analyzer then stays in memory, so later calls read nothing again. Loading is often most of an analyzer's running time, so calling the same analyzer on hundreds of nodes costs little more than the analysis itself. Its `.kb` files are not read: they are a complete saved knowledge base, and reading one into a knowledge base that already exists would add every attribute value a second time.

**What runs on each call.** The called analyzer's passes run in order on the subtree, with these differences from running on a text of its own:

- Tokenizer passes are skipped, because the tree already exists.
- A `dicttok` or `dicttokz` pass does not tokenize. Instead it looks up every word under `pnode` in the dictionaries, including the lazily loaded `*full` files, which only load a word once it is seen. Each word gets its dictionary attributes (such as `pos`), and multi-word dictionary phrases are matched among `pnode`'s children.
- Global variables (`G`) start empty on every call and are discarded afterwards, so the caller's global variables are neither visible nor changed.
- `G("$apppath")` is the called analyzer's folder.
- No per-pass `.tree` log files are written.

Error messages from the called analyzer go to the caller's `err.log`, numbered by the called analyzer's own passes.

**Writing an analyzer to be called.** Start its sequence with a `dicttok` pass. When it runs on its own, the pass tokenizes its input as usual; when it is called, the pass runs its dictionaries on the node it was given. Put its results under `callconcept()`, which also returns a concept when the analyzer runs on its own, so it can be developed and tested without a caller.

**Finding the analyzer.** `analyzerStr` is the name of the analyzer's folder. The folder is looked for beside the calling analyzer's folder, which is where analyzers sit in a VisualText workspace. A relative path is taken from that same place, and an absolute path is used as given. If an analyzer with that name is already loaded, it is reused.

**Calls that are refused.** An analyzer cannot call itself. It also cannot call an analyzer that is already running further up a chain of calls (for example, A calls B and B then calls A). In both cases `callanalyzer` returns 0.

When the NLP++ debugger is attached, it does not stop inside a called analyzer. The whole call is stepped over as one statement of the caller.

## Example

The calling analyzer hands each `_sent` node to an analyzer named `colors`:

```
@CODE
G("results") = makeconcept(findroot(),"results");
@@CODE

@POST
L("sent") = makeconcept(G("results"),"sent");
callanalyzer(N(1), L("sent"), "colors");

@RULES
_xNIL <- _sent @@
```

The `colors` analyzer sits in a folder beside the caller. Its `analyzer.seq` runs a `dicttok` pass and then this pass, which turns every word its dictionary marks as a color into a `_color` node and records the color:

```
@CHECK
if (!N("color",1))
	fail();

@POST
addstrval(callconcept(),"color",strtolower(N("$text",1)));
single();

@RULES
_color <- _xALPHA @@
```

After each call, the color words in that sentence are `_color` nodes in the caller's parse tree, and the `sent` concept holds their colors.

## See Also

[callconcept](callconcept.md), [findana](findana.md), [makeconcept](makeconcept.md), [Special Functions](Table_of_Special_Functions.md)
