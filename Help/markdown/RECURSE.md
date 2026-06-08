# RECURSE Region

The RECURSE Region is a nested "minipass" within a pass file. It can only be invoked from an element of a rule that has matched. The phrase that the recurse minipass operates on is the set of nodes that matched the invoking rule element. Each RECURSE Region contains within it a Grammar Region.

## Example of RECURSE Region

Here's an example taken from the RFA (Rules-File Analyzer), which parses the pass files themselves.

```
@RECURSE actionpass # Start of a RECURSE Region. A name, e.g. "actionpass", is required.
```

```
@RULES # Start of one RULES Regions within the RECURSE minipass.
```

```
# The minipass converts literals (e.g., "single") to actions in context.
```

```
_ACTION <- _LIT @@
```

```
@@RECURSE # End of the RECURSE minipass. Note that @@RULES is optional.
```

```
# .... # Additional RECURSE minipasses may be specified here.
```

```
# The GRAMMAR ZONE (i.e., the main Grammar Region of the pass file) starts here. It has no marker.

# Note that in this case, the @@RECURSE terminator is required, so that the main Grammar Region is not

# taken to be part of the previous RECURSE minipass.
```

```
@RULES
```

```
_POSTS [base] <- # Simplified rule for identifying a @POST Region.
```

```
_soPOST # @POST

_xWILD [matches=(_LIT _ACTION) recurse=(actionpass)]

_eoPOST [opt] # @@POST is optional.
```

```
@@
```

In the above example, when the NLP++ parser (RFA or RFB) sees a plain word like "single" in a file, it doesn't know whether to reduce it to an _ACTION or not. But within the markers @POST and @@POST, the literal should be treated as an action. This allows the parentheses in pass file actions to be optional, when the action takes no arguments. E.g., "single()" and "single" are equivalent.

In general, RECURSE mini-passes enable a mechanism for "roughing out" a text and then applying the correct assignments when the context has been determined unambiguously. They have many other uses, such as traversing nodes that matched a rule element in order to perform cleanups, data gathering, deletions, and so on.

For a phrase element modifier that invokes a recursive rules pass, see the [recurse](NLP_PP_Stuff/Phrase_element_modifiers.md#recurse) modifier.

| **Note**: A RECURSE Region cannot contain a CODE Region or a SELECT Region. A SELECT Region would be meaningless, since the RECURSE Region operates on a phrase specified by the rule element that invokes it. |
| --- |

## See Also

[Minipass Zone](NLP_PP_Stuff/Minipass_Zone.md)

[About Pass Files](NLP_PP_Stuff/About_Pass_Files.md)

[Grammar Region](NLP_PP_Stuff/Grammar_Region.md)
