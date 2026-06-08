# About Automated Rule Generation

VisualText allows you to enhance text analyzers by merely highlighting and categorizing samples from text. Automated rule generation (or **RUG**, for short) creates passes and rules for you automatically, so that you don't have to worry about the details of rule writing. It also makes analyzers much more maintainable, because when you modify an analyzer and then invoke RUG, it *automatically* updates rules according to changes made earlier on in the analyzer. That is, the developer doesn't need to worry that changes to rules in one pass will invalidate dependent rules in subsequent passes.

RUG is best used for word and phrase-level constructs that are modular and well defined, e.g., telephone numbers. More generally, RUG can be used for the things that an analyzer deals with explicitly. For example, a linguistically sophisticated analyzer that identifies the components of sentences (noun phrases, verb phrases, etc.) can exploit RUG to identify clausal and sentential patterns.

RUG is less useful for completely open ended or nonproductive constructs. For example, RUG might not be very useful for storing and identifying many instances of full names, such as "John Smith."

As you develop your text analyzer, you will learn how best to organize the samples that you want to collect within the Gram Tab.

## Controlling Automated Rule Generation

A caveat in using RUG is that sometimes rules will not be as general as you want, or they may be more general than you want. The [Gram Concept Properties](../Setting_Rule_Generation_Properties.md) dialog can be used to help control some of these behaviors. Updates to this Help documentation will help detail some settings, but experimentation may also be required.

## Automated Rule Generation and the Gram Tab

The [Gram Tab](../VisualText_Interface/Tab.md#Gram_Tab) is where you set up concepts and samples for the automated rule generation process.

## Basic Process of Automated Rule Generation

VisualText automatically generates rules by taking samples you provide, making generalizations from the samples, and then creating the rules. An outline of the process of automatic rule generation is given below.  **Each step is detailed in the Automatically Generating Pass Files section**.

1. Create a **stub**, (e.g., called phrases).

1. Select a pass in the Ana Tab at the location where you want a set of automatically generated passes to be placed. Then, either add a **stub concept** in the Gram Tab or a **stub region** in the Ana Tab, since adding one always adds the other automatically. The stub concept is the primary organizer of user-highlighted samples. The stub region is reserved for the automatically generated passes and rules. When RUG is invoked, it automatically inserts or overwrites passes within the stub regions.

1. We recommend that the ordering of stub concepts (in the Gram Tab) and their corresponding stub regions (in the Ana Tab) be kept in tandem, for clarity.

1. Create a **folder concept**, another level of organizing user samples (e.g., contact information).

1. Folder concepts organize multiple types of samples.

1. Create a **rule concept**, which represents a set of closely related samples (e.g., telephone number).

1. Rule concepts "own" a set of related samples.

1. Create a** label concept**, which represents a set of subsamples (e.g., area code).

1. Label concepts "own" a set of related subsamples. Label concepts and subsamples are optional. For example, if you don't care about subdividing a telephone number, then you need not create a label concept for the area code.

1. Select a **concept** in the Gram Tab (under which you want to add text samples).

1. This will dynamically create a menu of rule and label concepts, with which the user may categorize samples.

1. Highlight a **sample** within a text file in the workspace.

1. Use the Text Tab to find and open a text file, then highlight a text sample within it.

1. Right-click and select a rule or label concept.

1. For example, if a full telephone number sample is highlighted, select the rule concept for telephone numbers. If you highlight a part of the full sample, such as an area code, then select the label concept for area codes.

1. Invoke RUG.

1. When done adding samples and subsamples, from the Main Menu select Analyzer > Generate Rules > All. RUG will create new passes, as appropriate, in the stub regions of the Ana Tab. (You could also use the Generate button, but we recommend that Generate Rules > All be used as far as possible.)

## See Also

[Adding Stub Regions](../Using_VisualText/Automatically_Generating_Pass_Files/Adding_stub_regions.md)

[Adding Rule Concepts](../Using_VisualText/Automatically_Generating_Pass_Files/Adding_rule_concepts.md)

[Adding Folder Concepts](../Using_VisualText/Automatically_Generating_Pass_Files/Adding_folders.md)

[Adding Samples to Rule Concepts](../Using_VisualText/Automatically_Generating_Pass_Files/Adding_samples_to_rule_concepts.md)

[Adding Label Concepts](../Using_VisualText/Automatically_Generating_Pass_Files/Adding_Label_Concepts.md)

[Setting Concept Properties](../Using_VisualText/Automatically_Generating_Pass_Files/Setting_concept_properties.md)

[Running the Rule Generator](../Using_VisualText/Automatically_Generating_Pass_Files/Running_the_Rule_Generator.md)
