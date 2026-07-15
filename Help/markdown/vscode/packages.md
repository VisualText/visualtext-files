# Calling Analyzers from Python & Node.js

The NLP++ engine ships as a native package for both **Python** (`NLPPlus` on PyPI) and
**Node.js** (`nlpplus` on npm). Both link the engine's C++ libraries directly into the
process, so your program calls an analyzer **in‑process** — far faster than shelling out
to the command‑line `nlp` engine.

[← Back to Help home](home.md)

This page shows how to **call** an analyzer, **pass structured data into** it, and **get
data back out** of it. The analyzer itself is built and debugged in the VS Code NLP++
extension exactly as always — these packages just drive it from your own code.

## Install

```sh
pip install NLPPlus      # Python 3.10+
npm install nlpplus      # Node.js 18+
```

Both bundle the engine and a small set of starter analyzers (`parse-en-us`,
`address-parser`, `emailaddress`, `links`, `telephone`).

## Call an analyzer

The simplest call runs the default US‑English parser and returns its parse as text (XML):

**Python**
```python
import NLPPlus
xml = NLPPlus.analyze("Hello world.")
```

**Node.js**
```js
const nlpplus = require('nlpplus');
const xml = nlpplus.analyze('Hello world.');
```

`analyze(text, analyzer="parse-en-us", develop=False, compiled=False)` returns a
**Results** object (see below). To run one of *your* analyzers instead of a bundled one,
point the engine at your analyzers folder first:

**Python**
```python
NLPPlus.set_analyzers_folder(r"C:\path\to\my\analyzers")
results = NLPPlus.analyze("My phone is 123-456-7890.", "telephone")
```

**Node.js**
```js
nlpplus.setAnalyzersFolder("C:\\path\\to\\my\\analyzers");
const results = nlpplus.analyze("My phone is 123-456-7890.", "telephone");
```

> **Editing the bundled analyzers?** Copy them somewhere writable first with
> `copy_library_analyzers(dir)` / `copyLibraryAnalyzers(dir)` — otherwise a package
> upgrade overwrites your edits. That call also sets the analyzers folder to the copy.

## Getting data back

An analyzer returns results two ways, depending on whether it emits **text** or
**structured extractions**. The `Results` object exposes both.

| Python (`results.`) | Node.js (`results.`) | What it is |
|---|---|---|
| `output` | `output` | `output.json` parsed into a native object/dict — the usual way to read extractions |
| `output_json` | `outputJson` | the raw `output.json` text (string), or `None`/`null` |
| `output_text` | `outputText` | the analyzer's **text** output (what it streamed to `output.txt`) |
| `final_tree` | `finalTree` | the full NLP++ parse tree (`final.tree`) — handy for debugging |

### Extracted data → `output.json`

Domain analyzers (telephone, email, addresses, …) don't return text — they **build a
knowledge base (KB)** of what they found and serialize it to **`output.json`**. In NLP++
this is done in a final pass with the `KBFuncs` library's `JsonKB` function, e.g.
`JsonKB("output.json", G("telephone"));`. Read it back as a native object:

**Python**
```python
results = NLPPlus.analyze("Call 123-456-7890 or (222) 333-4444.", "telephone")
for phone in results.output["telephones"]["telephone"]:
    print(phone)
```

**Node.js**
```js
const results = nlpplus.analyze("Call 123-456-7890 or (222) 333-4444.", "telephone");
for (const phone of results.output.telephones.telephone) {
  console.log(phone);
}
```

`results.output` is `None`/`null` if the analyzer never wrote an `output.json` — so an
analyzer you want to call this way **must** include an output pass that writes it. (This
is the same `output.json` that [regression testing](testing.md) compares.)

### Text → `output.txt`

An analyzer that produces **text** rather than records writes it in NLP++ with the
special output stream `"output.txt" << ...`. That streamed text comes back as
`results.output_text` / `results.outputText`. The default `parse-en-us` parser uses this
path to return its XML parse.

## Passing data *into* an analyzer

Sometimes an analyzer needs reference data at run time — a list of companies, a product
catalog, a lookup table. You hand it **JSON**, and the analyzer loads it into its
knowledge base.

**Two things are required — both are mandatory, neither works without the other:**

1. **The data must be stored in the analyzer's `kb/` directory using the package
   function for this.** Don't copy files there by hand — call `put_json_object` /
   `put_json_file` (Python) or `putJsonObject` / `putJsonFile` (Node), which write the
   JSON into `<analyzer>/kb/user/`.
2. **The analyzer being called must have the `json2kbb` python script in its sequence,
   placed *before the tokenizer*.** This pass is what converts the JSON in `kb/user/`
   into a `.kbb` knowledge‑base file the engine loads on the run. If it isn't in the
   sequence (before the tokenizer), the JSON is written but **never loaded into the KB**.

### Step 1 — add the `json2kbb` pass to the analyzer (one time)

In the VS Code NLP++ extension, open the **Sequence** view and **right‑click the
tokenizer** (or any pass) → **Insert Python Library Pass (Before Tokenizer)** → choose
**`json2kbb`**. It must run **before the tokenizer** so the data is in the KB before
analysis begins. Without this pass the JSON is written but never loaded.

### Step 2 — hand it the JSON from your code

**Python**
```python
# From a Python object...
NLPPlus.put_json_object("myanalyzer", {"company": {"name": "Acme Corp"}}, "company")
# ...or from an existing JSON file:
NLPPlus.put_json_file("myanalyzer", "data/company.json")

# Now analyze — the json2kbb pass builds company.kbb into the KB first.
results = NLPPlus.analyze("Acme Corp shipped the order.", "myanalyzer")
```

**Node.js**
```js
nlpplus.putJsonObject("myanalyzer", { company: { name: "Acme Corp" } }, "company");
// or: nlpplus.putJsonFile("myanalyzer", "data/company.json");
const results = nlpplus.analyze("Acme Corp shipped the order.", "myanalyzer");
```

- `putJsonObject(analyzer, obj, name)` serializes any JSON‑serializable value to
  `<analyzer>/kb/user/<name>.json`.
- `putJsonFile(analyzer, path, name?)` copies an existing JSON file in (defaulting the
  name to the source file's name).

### How the JSON becomes knowledge

On the next run, `json2kbb` converts each `<name>.json` into `<name>.kbb`, which is the
inverse of the `JsonKB` serializer above:

| JSON | KBB (knowledge base) |
|---|---|
| an object | a concept |
| `"key": <value>` (primitive) | an attribute: `key=value` |
| `"key": { … }` | a child concept `key:` |
| `"key": [ … ]` | counted children `key1:`, `key2:`, … |

```text
{ "company": { "name": "Acme Corp", "founded": 1990,
    "dept": [ {"name":"Eng"}, {"name":"Sales"} ] } }
```
becomes
```text
company: name="Acme Corp", founded=1990
  dept1: name=Eng
  dept2: name=Sales
```

> **Re‑running with changed data:** `json2kbb` only builds a `.kbb` when one doesn't
> already exist (so it never clobbers a hand‑edited KB). To pick up an edited JSON,
> delete the matching `<name>.kbb` first, then run again. `put_json_object` overwrites
> the `.json`, so a fresh working folder always rebuilds cleanly.

## A full round trip

Pass data in, analyze, read structured data back — with proper cleanup of the engine.

**Python** (context manager closes the engine for you)
```python
from NLPPlus import Engine

with Engine() as eng:
    eng.set_analyzers_folder(r"C:\path\to\analyzers")
    eng.put_json_object("myanalyzer", {"skus": ["A1", "B2"]}, "catalog")
    results = eng.analyze("Order for A1 and B2.", "myanalyzer")
    print(results.output)        # parsed output.json
    print(results.output_text)   # any text the analyzer emitted
```

**Node.js** (call `close()` in a `finally`)
```js
const { Engine } = require('nlpplus');
const eng = new Engine();
try {
  eng.setAnalyzersFolder("C:\\path\\to\\analyzers");
  eng.putJsonObject("myanalyzer", { skus: ["A1", "B2"] }, "catalog");
  const results = eng.analyze("Order for A1 and B2.", "myanalyzer");
  console.log(results.output);
  console.log(results.outputText);
} finally {
  eng.close();
}
```

> **Always close an `Engine` you create explicitly.** On Windows the engine keeps a file
> handle open in its working folder, and `close()` (or the Python `with` block) is what
> lets an auto‑created temporary working folder be removed. `close()` is idempotent.

## Developing against your VS Code analyzer

`input_text(analyzer, file_name)` / `inputText(analyzer, fileName)` reads a file from the
analyzer's `input/` directory — the same test text you use in the extension — so your
script and the VS Code analyzer stay in sync while you develop:

**Python**
```python
text = NLPPlus.input_text("telephone", "test.txt")
results = NLPPlus.analyze(text, "telephone")
```

## Running compiled analyzers

By default analyzers run **interpreted** from their `.nlp` source. For speed (or to ship
without source) you can compile an analyzer to a native shared library and load it with
`compiled=True`:

**Python**
```python
NLPPlus.cloud_compile("myanalyzer")            # build via the cloud service
xml = NLPPlus.analyze("…", "myanalyzer", compiled=True)
```

**Node.js**
```js
await nlpplus.cloudCompile("myanalyzer");
const xml = nlpplus.analyze("…", "myanalyzer", false, true);
```

See **[Compiling Analyzers](compiling.md)** for what compiling does and the one‑click
path in the extension.

## More help

- **[Regression Testing](testing.md)** — the `output.json` these packages read is the
  same file golden‑file tests compare.
- **[Compiling Analyzers](compiling.md)** — turn an analyzer into a fast native library.
- Package pages: **[NLPPlus on PyPI](https://pypi.org/project/NLPPlus/)** ·
  **[nlpplus on npm](https://www.npmjs.com/package/nlpplus)**.
