[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# makeliteral

## Purpose

Replace a range of rule elements with one token whose text you give. Later passes treat it like any token of its type.

## Syntax

```
makeliteral(startNum, endNum, textStr)
makeliteral(startNum, endNum, textStr, typeStr)
```

```
startNum - type: int, first rule element to replace
endNum - type: int, last rule element to replace
textStr - type: str, the new token's text
typeStr - type: str (optional): num, alpha, punct, white, ctrl, emoji or node
```

## Returns

Nothing is returned to NLP++. As a side effect, the nodes matching rule elements *startNum* through *endNum* are replaced by one token. Its name and `$text` are *textStr*. It keeps the offsets of the nodes it replaced, so it still points at the original text in the input.

## Remarks

Without *typeStr*, the token gets the type the tokenizer would give *textStr*: all digits makes **num**, all whitespace makes **white**, a single punctuation character makes **punct**, and anything else makes **alpha**.

Like [singlezap](singlezap.md), **makeliteral** removes the nodes it replaces, so it should be the last action in the POST region.

**NEW 4.2.28**

## Example

OCR sometimes reads the number 70 as "7O", with a letter O. This turns it back into a number:

```
@POST
  makeliteral(1, 2, "70");
@RULES
_xNIL <- 7 O @@
```

Later passes see a **num** token "70". A rule such as `_money <- _xNUM _xWHITE [s] dollars @@` matches it, and its `$text` is "70".

To force a type, give it as a fourth argument, as in `makeliteral(1, 1, "USA", "alpha")`.

## See Also

[singlezap](singlezap.md), [singler](singler.md), [single](single.md), [POST Actions](NLP_PP_Stuff/AT-POST_Actions.md#table_of_@POST_Actions)
