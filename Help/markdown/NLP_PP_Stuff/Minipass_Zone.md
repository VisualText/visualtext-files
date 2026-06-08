# Minipass Zone

The Minipass Zone is used to write zero or more nested "minipasses" within a pass file. Each minipass is called a RECURSE Region and has an associated name. The Grammar Region within a RECURSE Region is not executed directly, but rather it is invoked by a **recurse** element action when a rule elsewhere in the pass file has matched.

The idea is that a rule element, such as a wildcard, "roughs out" a segment or phrase of nodes by matching or collecting these nodes. Then that rule element invokes a minipass by name in order to characterize or refine the matched phrase.

Typically, minipasses are invoked from rules in the main Grammar Zone of the pass file. But matches in one RECURSE Region may lead to invoking a second RECURSE Region.

## See Also

[About Pass Files](About_Pass_Files.md)

[RECURSE Region](../RECURSE.md)
