# Lazy Loading

**Lazy loading** keeps an analyzer's startup fast and its memory footprint small by
bringing knowledge-base data into memory **only when it's needed**, instead of loading
everything up front. This matters most for large dictionaries and knowledge bases.

[← Back to Help home](home.md)

There are two sides to it: the engine's **automatic** dictionary lazy-loading, and the
**on-demand** loading you control from your rules.

## Automatic dictionary lazy-loading (Version 3+)

Since **Version 3**, the engine can load dictionary/KB words **individually, as they are
encountered**, rather than reading an entire lexicon at startup — giving **faster startup
and a smaller memory footprint** for large dictionaries.

> 🔑 **Lazy loading only kicks in for files named `…full.dict` or `…full.kbb`.**
> The file name must end in **`full`** before the extension — for example `en-full.kbb`,
> `pt-full.dict`, `pt-verbs1200-full.kbb`. For a file named this way the engine pulls in
> words on demand instead of loading the whole file up front. Files **not** named `…full`
> load normally (all at once). So: name your large dictionary/KB files `…full.dict` /
> `…full.kbb` to get lazy loading.

### Which English library files are lazy

The rule is the file name, and `full` has to be the **last** part of it, so a name can
contain the word and still load eagerly. `en-full-feat.dict` ended in `feat` and was
read whole at startup for that reason alone.

In `languages/English` the lazily loaded files are `en-full.dict`, `en-full.kbb`,
`en-feat-full.dict`, `en-lemmas-full.kbb` and `en-synonyms-full.kbb`. Still eager,
because nothing in this repository loads them into an analyzer yet: `en-nouns.dict`
(2 MB) and `en-roots.kbb` (4 MB). Rename them the same way when something does.

Measured with one file in `kb/user` and a 60-word input:

| file in `kb/user` | size | dictionary read |
|---|---|---|
| `en-full.dict` | 3.8 MB | 0.19 s |
| the featured dictionary under its old name | 8.3 MB | 1.76 s |
| the same bytes as `en-feat-full.dict` | 8.3 MB | 0.21 s |

Renaming `en-lemmas.kbb` is what this is worth in a real analyzer rather than a
benchmark: EnglishPhrases pulls it in with `loadkbb` and went from 5.32 s to 0.70 s
on the same input, with `phrases.txt` byte-identical across all 52 of its inputs and
the same 749 lemmas resolved — so the lazily loaded table answered every lookup the
eager one did.

The attributes arrive on the node either way — a lazily loaded featured dictionary
still gives a word its `vform`, `tense` and `number`. Only the timing changes.

## Loading a KB or dictionary on demand

When only some inputs need a large domain knowledge base or dictionary, you can load it
**on demand** from the analyzer's `kb/user` directory, rather than always loading it at
startup:

| Function | Loads | File format |
|---|---|---|
| [`loadkbb("file.kbb")`](../loadkbb.md) | a `.kbb` knowledge base | indented hierarchy ("dictionary" format) |
| [`loaddict("file.dict")`](../loaddict.md) | a `.dict` dictionary | flat `word attr=val …`, one word per line |

Both take a **file name in `kb/user`** (not a full path), add the contents to the KB
already in memory, and return **1** on success / **0** if the file wasn't found.

### Example — load a heavy KB only the first time it's needed

```
@CODE
if (!num(G("loadedMedical"))) {
    if (loadkbb("medical.kbb"))
        G("loadedMedical") = 1;
}
@@CODE
```

Guarding with a global (`G("loadedMedical")`) ensures the file is loaded **once**, the
first time that code path runs, and skipped afterwards.

## When to use it

- A large domain KB / dictionary that only certain analyzers or certain inputs need.
- Faster startup: keep the base KB small and pull in the heavy pieces on first use.

## See also

[loadkbb](../loadkbb.md) &nbsp;|&nbsp; [loaddict](../loaddict.md) &nbsp;|&nbsp;
[Knowledge Base Functions](../Table_of_Knowledge_Base_Functions.md) &nbsp;|&nbsp;
[Compiling Analyzers](compiling.md)