# unsealed

## Purpose

In a normal rule reduction, the suggested node is "sealed".  This makes it inaccessible to the @NODES selection mechanism, which looks for nodes in the parse tree, then takes their phrase of children to use in searching for rule matches.  In order to make a node accessible to be "looked inside of" by the context selection algorithm, you can use the **unsealed** suggested element modifier.

## Remarks

Unsealed is not related to the singlet-base mechanism described elsewhere.

The @NODES selector starts at the root of the parse tree, then looks only within *a path of unsealed nodes* for appropriately labeled nodes within which to perform rule matching.  So keep nodes unsealed that you want to look within.  Note that the @PATH selector does not care if nodes are sealed or not.

## Example

# This rule "roughs out" a set of nodes ending in a period, creating a _sentence node. # This rule also makes such a _sentence node accessible to further rule matching. @RULES _sentence [unsealed] <-  _xWILD [fail=( \. )] \. @@ # Say that in a subsequent pass (shown below), we want to process _np nodes within _sentence # nodes in order to count the nouns within noun phrases.  The @NODES _np # specifier will only look for _np nodes within ancestors that are *unsealed*.  If the # sentence rule above doesn't use unsealed, then noun phrases within those # sentences won't be traversed. @NODES _np @POST  ++X("nouns"); @RULES _xNIL <- _noun @@

## See Also

See [Suggested Element Modifiers](NLP_PP_Stuff/Suggested_element_modifiers.md).
