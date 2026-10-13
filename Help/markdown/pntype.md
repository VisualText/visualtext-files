[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# pntype

## Purpose

Fetch the token type of a parse tree node *aPnode*.

## Syntax

```
returnedString = pntype(aPnode)
```

```
returnedString - type: str

aPnode - type: pnode
```

## Returns

For a token (a leaf node made by the tokenizer), one of:

| Type | Token |
|---|---|
| `alpha` | Alphabetic, including accented and other Unicode letters |
| `num` | Digits |
| `punct` | Punctuation |
| `white` | Whitespace |
| `ctrl` | Control character |
| `emoji` | Emoji |

For a nonleaf node, one built by a rule such as `_np`, it returns `node`.

These are the same names the parse tree display shows after each node.

## Remarks

Use `pntype` when code walks the tree with [pndown](pndown.md) and [pnnext](pnnext.md) and needs to know what kind of token it is looking at. Rule elements such as `_xALPHA` and `_xPUNCT` only test the type while matching a rule; `pntype` answers the same question for any node in code.

**NEW 4.2.10**

## Example

```
@CODE

L("n") = pndown(pnroot());
while (L("n")) {
    if (pntype(L("n")) != "white")
        "tokens.txt" << pnname(L("n")) << "\t" << pntype(L("n")) << "\n";
    L("n") = pnnext(L("n"));
}

@@CODE
```

For the input `Hi 42, 🔥!` this writes:

```
Hi	alpha
42	num
,	punct
🔥	emoji
!	punct
```

## See Also

[pnname](pnname.md), [pnvartype](pnvartype.md), [pndown](pndown.md), [pnnext](pnnext.md), [Parse Tree Functions](Table_of_Parse_Tree_Functions.md)
