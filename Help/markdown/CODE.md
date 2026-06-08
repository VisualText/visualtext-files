[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# CODE Region

The Code Zone may optionally contain a single CODE Region, which begins with the @CODE marker and optionally terminates with the @@CODE marker.

NLP++ code in the CODE Region is executed prior to any rule matching for the current pass.

The CODE Region may, in addition to NLP++ code syntax, incorporate CODE Actions, i.e., specialized functions that are constrained to the CODE Region.

The **exitpass()** function is useful for conditionally and immediately terminating the current pass, without executing any rules.

## See Also

[CODE Zone](NLP_PP_Stuff/Code_Zone.md)

[CODE Action](NLP_PP_Stuff/AT-CODE_Actions.md)
