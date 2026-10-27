# Large Files

An analyzer meets two kinds of large file: a **large input**, such as a long tax
return package or a book, and a **large dictionary or knowledge base**, such as a
full English lexicon or a code index. They grow differently, so they are handled
differently: a large input with **zone mode**, a large dictionary or KB with
**lazy loading**.

[← Back to Help home](home.md)

## Large inputs

### Why size matters

The engine reads an input whole and builds **one parse tree** for it, and every
pass works on that tree. Memory and time therefore grow with the document and with
the analyzer. Measured on 64-bit Windows:

| Analyzer | Memory per MB of input | Time per MB of input |
|---|---|---|
| tokenizer and one pass | about 60 MB | 1 to 3 seconds |
| parse-en-us (130+ passes) | about 700 MB | about 4 minutes |

Both grow in a straight line: twice the text takes twice the memory and twice the
time. A document of a few hundred KB is no trouble; tens of MB with a large
analyzer can exhaust memory.

The largest input the engine accepts is **2,000,000,000 bytes**, on every
platform. A larger file is refused with a message on stderr.

### Zone mode (engine 4.2.47)

Zone mode handles a large input the way a person reads one: **skim** it to find its
parts, **read** each part in turn and keep what it says, then **wrap up**. A `zone`
line in `analyzer.seq` names a node type, and every pass after it runs once for
each node of that type:

```
tokenize  nil
nlp       lines         # skim: one node per line, form headers marked
nlp       forms         # skim: one _form per form or schedule
zone      _form         # the passes below run once per _form
nlp       fields        # per form: find the values it holds
rec       amounts       # ...
endzone   nil           # the passes below run once, at the end
nlp       summary       # the whole package
```

How it works:

- **Skim.** The passes before the `zone` line run over the whole document, as
  usual, and build the zone nodes. Keep them cheap: lines, headings, blank lines,
  layout. A zone node inside another zone node is not a separate zone.
- **Read.** Each zone then runs the passes after the `zone` line **on its own**.
  Everything outside the zone is hidden, so its rules, `@PATH _ROOT ...` and
  `@CODE` work as they would on a document that is just that zone. `@CODE` and
  `@POSTCODE` run once per zone, and `G("$isfirstzone")` and `G("$islastzone")` are
  1 in the first and last zone.
- **Keep what it says.** The KB and `G()` carry from zone to zone, as they do from
  file to file in a folder run. Node offsets count from the start of the document,
  and there is one set of output files.
- **Let the tree go.** After its passes a zone keeps its node, attributes and span,
  and the tree under it is freed. While a zone runs, the other zones are hidden,
  earlier ones included.
- **Wrap up.** The passes after an `endzone` line run once, after the last zone, on
  the zone nodes and the whole KB. Put whole-document work there: totals, a summary,
  dumping the KB.

### What memory goes by

Peak memory in zone mode is the larger of two things:

- **The skim tree.** The passes before the `zone` line build a tree of the whole
  document, at least its tokens, and that tree exists before any zone runs. Zones
  cannot free it. Keep the skim passes few and cheap.
- **The largest zone.** Each zone's full tree exists only while its passes run.

So zone mode only works as well as the skim divides the document. Look at the zone
spans in `final.tree`: if one zone covers most of the document, that zone is
analyzed whole and memory is barely lower than without zones.

parse-en-us runs in zone mode by default from v1.1.5, one zone per paragraph
(`_TEXTZONE`). On two novels, peak memory and time:

| Book | Without zones | Zoned |
|---|---|---|
| *Pride and Prejudice*, 738 KB, 127,360 words | 473 MB, 275 s | 153 MB, 283 s |
| *War and Peace*, 3.3 MB, 563,286 words | 1,910 MB, 1,120 s | 455 MB, 1,106 s |

Zoning takes about the same time either way. *War and Peace* ran on a 32-bit
build, whose limit is 2 GB: without zones it used almost all of it, so a somewhat
longer book would have failed, while zoned it used under a quarter. Its final
tree went from 345 MB to 1.3 MB.

On *Pride and Prejudice*, 99.995% of words got the same part-of-speech tag and the
KB at the end was byte-identical. On *War and Peace*, 97.5% did; the changes go
both ways, and the zoned run leaves fewer words UNKNOWN (1.6% against 2.1%).
*War and Peace* is about 4.4 times longer, so its skim tree is too, and that, not
its paragraphs, sets its 455 MB.

*War and Peace* also showed the cost of one oversized zone. In parse-en-us before
v1.1.6, a line starting `1.` inside running text (Tolstoy's list of the seven
Freemason virtues) began a zone that ran to the end of the book: 2.3 MB, 71% of it.
Zoned, memory fell only to 776 MB. The same huge "paragraph" had also left 18% of
the book's words tagged UNKNOWN, with or without zones. With the zone stopping at
the next paragraph, the largest zone is 4.4 KB and 1.6% of words are UNKNOWN.

### Example: one zone per form

A tax return package is a stack of forms and schedules: the main return, its
schedules, then attached forms, each starting with a header line. One form never
needs another form's parse tree, so each form makes a natural zone. These two skim
passes build them:

```
# lines.nlp: one node per line; a line that starts a form is a _formStart.
@NODES _ROOT

@RULES
_formStart <-
	_xWILD [one matches=(Form FORM Schedule SCHEDULE)]
	_xWILD [star fails=(\n)]
	\n
	@@

_line <-
	_xWILD [plus fails=(\n)]
	\n
	@@
```

```
# forms.nlp: a _form runs from a form's header line to the next one.
@NODES _ROOT

@RULES
_form <-
	_formStart
	_xWILD [star fails=(_formStart)]
	@@
```

After `zone _form`, a pass sees one form at a time under `_ROOT`. A per-form pass
records what it finds in the KB or `G()`, and the `summary` pass after `endzone`
reports on the whole package:

```
# fields.nlp, after the zone line: runs once per form.
@CODE
G("forms")++;
L("form") = pndown(pnroot());       # the one form in view
"forms.txt" << strtrim(pnvar(pndown(L("form")),"$text")) << "\n";
@@CODE
```

```
# summary.nlp, after the endzone line: runs once.
@CODE
"forms.txt" << G("forms") << " forms" << "\n";
@@CODE
```

Text before the first header, such as a cover page, is in no zone: it gets the
skim passes only. Make the skim cover everything you need, or add a rule that
makes the cover page a `_form` of its own.

### Writing an analyzer for zone mode

- **Pick zones that stand alone.** A paragraph, a form, a section, a page: a part
  whose analysis does not need another part's tree. Anything a later zone needs
  from an earlier one goes in the KB or `G()`.
- **Mind @CODE.** It runs once per zone now. Code that sets up the document goes
  before the `zone` line, or checks `G("$isfirstzone")`. Code that writes one file
  for the whole document (a header, a closing tag, a KB dump) goes after `endzone`.
  A pass that does whole-document work in every zone grows with the KB: a KB dump in
  every paragraph of a book made a 26-second run take 181 seconds.
- **Change only the zone.** A pass after the `zone` line may change anything inside
  its zone, but not the tree above it, such as grouping `_form` nodes into a
  `_package`. That stops the run with an error, because the other zones can no longer
  be put back. Do that grouping in the skim passes.
- **Debugging.** With `-DEV`, the first three zones write their pass trees as
  `z001-ana040.tree`, `z002-ana040.tree` and so on; later zones write none, which
  keeps a run over thousands of zones from writing hundreds of thousands of files.
  `final.tree` shows the zone nodes.
- **No zones found.** If the skim builds no node of the zone type, the passes after
  the `zone` line run on the whole document, and a warning says so.
- **Compiled analyzers** run zones the same way, from engine 4.2.49. Before that
  they ignored the `zone` and `endzone` lines and ran every pass on the whole
  document.

### Splitting a file into pieces

Without zone mode, a document can be split into files and streamed through one
run with `-STDIN`: the analyzer loads once and the KB carries from piece to piece.
Each piece gets its own tree and output folder, and offsets count from the start of
the piece. List the pieces in order, since a folder run takes files in whatever
order the file system gives them:

```
ls pieces/part*.txt | nlp -ANA <analyzer> -WORK <workdir> -STDIN
```

`$isfirstfile` and `$islastfile` mark the first and last piece. Programs that start
`nlp` from .NET or PowerShell need engine 4.2.47 or later, which ignores the UTF-8
byte-order mark .NET writes ahead of the first path.

### Safety limits

Two limits keep a run on a large input from going on forever:

- **`-TIMELIMIT <seconds>`** stops a run that takes longer, with a message on stderr
  and exit code 2.
- **The rec pass limit.** A `rec` pass repeats while any rule matches, so a rule that
  keeps matching without changing anything used to repeat forever. From 4.2.47 a
  region may take 1,000 matches plus 20 per node in it; past that the region is
  stopped, the rest of the pass goes on, and stderr names the pass, the rule's line
  and the input. Set `NLP_REC_LIMIT` to scale the limit, or to `0` to lift it.

Leave `-DEV` off when timing a large input: it writes the whole tree after every
pass, which on parse-en-us makes a run take about 3.6 times as long.

## Large dictionaries and knowledge bases

A large dictionary or KB is a different problem: its size is in the KB, not the
input, so it costs startup time and memory on every run, even for a one-line
input. The answer is to load only what the input uses. **[Lazy Loading](lazyload.md)**
covers this in full; in short:

- **Name it `…full.dict` or `…full.kbb`.** A file in `kb/user` whose name ends in
  `full` before the extension (`en-full.dict`, `pt-verbs1200-full.kbb`) stays on
  disk and is searched when a key is needed, instead of being read at startup. An
  8.3 MB dictionary went from 1.76 s to 0.21 s to read.
- **The tokenizer** looks every word of the input up in a lazy *dictionary*: a
  `…full.dict`, or a `…full.kbb` whose top concept is `dictionary` or that has a
  `.dict` file of the same name beside it.
- **Any pass** can look up a key in any lazy `…full.kbb` with
  [findconcept](../findconcept.md) or [getconcept](../getconcept.md) on its top
  concept (engine 4.2.39). The key is loaded with everything under it; a missing key
  is remembered, so it is searched only once. [down](../down.md) on the top concept
  loads the whole file, so use it only when you need every key.
- **On demand.** [loadkbb](../loadkbb.md) and [loaddict](../loaddict.md) load a KB or
  dictionary that only some inputs need, the first time the analyzer needs it.
- **Lines of any length.** From 4.2.38, `.kbb` and `.dict` lines and values load
  whatever their length.
- **Compiled analyzers** leave `…full` files out of the compiled KB and search them on
  disk the same way, so a compiled analyzer can ship a large lexicon as a `…full`
  file in `kb/user`.

## Checklist

| The input... | Do this |
|---|---|
| is a few hundred KB or less | nothing: run it whole |
| has parts that stand alone (forms, sections, paragraphs) | zone mode: a skim pass, `zone _part`, `endzone` |
| is zoned but memory barely drops | look in `final.tree` for one zone covering most of the document, and fix the skim |
| comes as many files, or must be split | stream the pieces through `-STDIN` |
| might hit a looping rule or run too long | `-TIMELIMIT`; the rec pass limit is on by default |
| uses a large dictionary or KB | name it `…full.dict` / `…full.kbb`; look keys up with `findconcept` |

## See also

[Lazy Loading](lazyload.md) &nbsp;|&nbsp;
[The analyzer sequence](../VisualText_Basics/About_the_analyzer_sequence.md) &nbsp;|&nbsp;
[Special variables](../NLP_PP_Stuff/Special_Variables.md) &nbsp;|&nbsp;
[$isfirstfile](../$isfirstfile.md) &nbsp;|&nbsp; [$islastfile](../$islastfile.md) &nbsp;|&nbsp;
[Calling Analyzers from Python & Node.js](packages.md)
