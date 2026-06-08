[← Help Contents](index.md) | [📘 NLP++ Textbook](NLP++_Textbook.md)

# RULES Region

The RULES Region is where you write the actual NLP++ rules.  The RULES Region begins with the @RULES marker and optionally terminates with the @@RULES marker.

Action Regions (i.e. PRE, CHECK, and POST) that precede a RULES Region apply to every rule within the RULES Region.

A RULES Region with no preceding Action Regions gets the default reduce action, **single**() applied to every rule match within it.

## Common Error: Not Resetting Actions

In order to reset the actions that apply to a RULES Region, one must reset actions by adding a @RULES marker before the rules to be reset.

**Example:**

@POST N("noun", 3) = "true";

single(); @RULES _np <- _det _quan _xALPHA @@ _np <- _det _xALPHA @@

In the above, we want to mark alphabetic tokens as possible nouns based on their context. But the code in the POST Region sets a variable called "noun" to "true" in the node matching the THIRD element of each rule in the RULES Region. However, this will fail, since the second rule has only two elements on the right hand side. Therefore, this example must be rewritten as

@POST N("noun", 3) = "true";

single(); @RULES _np <- _det _quan _xALPHA @@

@POST N("noun", 2) = "true";

single(); @RULES _np <- _det _xALPHA @@

It's even easier to forget to add a lone @RULES so as to reset to the default action for subsequent rules.

## See Also

[Grammar Region](NLP_PP_Stuff/Grammar_Region.md)

[Rule Syntax](NLP_PP_Stuff/Rule_syntax.md)

[PRE Region](PRE.md)

[CHECK Region](CHECK.md)

[POST Region](POST.md)
