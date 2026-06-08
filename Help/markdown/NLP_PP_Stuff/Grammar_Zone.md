[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Grammar Zone

The Grammar Zone is where you place the main rules of a pass file.

The Grammar Zone occurs as the last zone (or possibly the only zone) of a pass file.  Unlike other zones, the Grammar Zone does not have a distinguishing marker.

## Grammar Region

The Grammar Zone contains zero or more Grammar Regions.  The Grammar Region is where rules and actions may be written.

## Invoking Minipasses

If a pass file contains RECURSE Regions, then at least one rule in the Grammar Zone must invoke a RECURSE Region to "start the ball rolling", or no minipasses will ever be executed.  See the phrase element modifier, [recurse](Phrase_element_modifiers.md#recurse).)

## Common Error:  No Grammar Zone with RECURSE Region

Since a Grammar Zone has no beginning marker, a problem can occur if a pass file looks like:

@RECURSE abc

@RULES

...

#Intended start of Grammar Zone.

@RULES

In the above example, the last RULES Region is understood as part of the previous RECURSE Region, rather than as the start of the Grammar Zone.  To obtain the right reading, the RECURSE Region terminator should be used.

@RECURSE abc

@RULES

...

@@RECURSE

#Intended start of Grammar Zone.

@RULES

## See Also

[About Pass Files](About_Pass_Files.md)

[Grammar Region](Grammar_Region.md)

[PRE Region](../PRE.md)

[CHECK Region](../CHECK.md)

[POST Region](../POST.md)

[RULES Region](../RULES.md)
