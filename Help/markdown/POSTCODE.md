[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# POSTCODE Region

The Code Zone may contain a POSTCODE Region, which begins with the @POSTCODE marker and optionally ends with the @@POSTCODE marker.

NLP++ code in the POSTCODE Region runs *after* the current pass has finished matching its rules. The CODE Region is its counterpart, which runs *before* rule matching. Use POSTCODE to report on or clean up after what the rules just did. Before this region existed, that meant a separate pass made only of a CODE Region.

## Remarks

- **Placement:** the POSTCODE Region can come right after the CODE Region or at the end of the pass file. A pass file may also consist of nothing but a POSTCODE Region.
- **Pass types:** works in `nlp` and `rec` passes.
- **Variables:** sees the same variables as the CODE Region: global `G()` variables, local `L()` variables, and functions from the DECL Region. Like the CODE Region, it has no current node, so it uses functions such as [pnroot](pnroot.md) to reach the parse tree.
- **exitpass():** when the CODE Region calls [exitpass](exitpass.md), the pass skips its rules and its POSTCODE Region too. An **exitpass()** inside the POSTCODE Region just ends that region.

**NEW 4.2.19**

## Example

Count the letters a pass reduces, then report the count once the pass is done:

```
@CODE
G("letters") = 0;
@@CODE

@POSTCODE
"output.txt" << "letters: " << G("letters") << "\n";
@@POSTCODE

@NODES _ROOT

@POST
  G("letters") = G("letters") + 1;
  single();
@RULES
_letter <- _xALPHA @@
```

For the input `a b c` this writes `letters: 3`.

The POSTCODE Region can also end the file:

```
@NODES _ROOT

@POST
  single();
@RULES
_pair <- _letter _xWHITE [s] _letter @@

@POSTCODE
L("n") = pndown(pnroot());
while (L("n")) {
    if (pnname(L("n")) == "_pair")
        "output.txt" << "pair: " << pnvar(L("n"), "$text") << "\n";
    L("n") = pnnext(L("n"));
}
```

## See Also

[CODE Region](CODE.md)

[Code Zone](NLP_PP_Stuff/Code_Zone.md)

[@POSTCODE](@POSTCODE.md), [@@POSTCODE](@@POSTCODE.md)
