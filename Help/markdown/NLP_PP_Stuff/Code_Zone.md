[← Help Contents](../index.md) | [📘 NLP++ Textbook](../NLP++_Textbook.md)

# Code Zone

The Code Zone is reserved for regions of NLP++ code that are independent of rule matching.

## Code Region

The CODE Region is delimited by @CODE and (optionally) by @@CODE, and operates *before* any rule matching is executed for the current pass file.

A pass file may consist entirely of a Code Region.

## Postcode Region

The POSTCODE Region is delimited by @POSTCODE and (optionally) by @@POSTCODE, and operates *after* the current pass file has finished matching its rules. It may follow the CODE Region or end the pass file.

**NEW 4.2.19**

## See Also

[CODE Region](../CODE.md)

[POSTCODE Region](../POSTCODE.md)

[CODE Action](AT-CODE_Actions.md)
