# ****Grammar Region

A Grammar Region is where you write NLP++ rules and actions.

## Region Marker and Action Regions

The Grammar Region consists of one or more @RULES markers with associated rules and optionally with associated action regions.  These action regions are the PRE Region, the CHECK Region, and the POST Region.  (See below.)

## Grammar Zone in RECURSE Region

A RECURSE Region and the main Grammar Zone are the locations in which a Grammar Region may appear.

## Grammar Region "Subregions"

The following "subregions" may appear within a Grammar Region, anchored by the RULES Region:

| **REGION** | **DESCRIPTION** |
| --- | --- |
| **@PRE** | Actions that represent additional conditions on the matching of individual rule elements. **NOTE: **Does not allow general NLP++ code. |
| **@CHECK** | When a rule has matched, NLP++ code in this region checks for self-consistency and/or builds semantic data. A rule match may still be rejected from this region. |
| **@POST** | NLP++ code that operates once a rule match has been accepted. |
| **@RULES** | Contains the actual NLP++ rules. |

The end markers @@PRE, @@CHECK, @@POST, and @@RULES are optional.

## See Also

[PRE Region](../PRE.md)

[PRE Action](AT-PRE_Actions.md)

[CHECK Region](../CHECK.md)

[CHECK Action](AT-CHECK_Actions.md)

[POST Region](../POST.md)

[POST Action](AT-POST_Actions.md)

[Grammar Zone](Grammar_Zone.md)
