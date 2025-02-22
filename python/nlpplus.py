import NLPPlus
import json

# To install NLPPlus, you need to download the latest wheel file from the
# NLPPlus GitHub releases page and install it using pip. Here is the link:
# https://github.com/VisualText/py-package-nlpengine/releases/latest
# Choose the version that matches your operating system and instll it using pip:
# pip install nlpplus-<version>.whl

# This example uses the Telephone Numbers analyzer.
# You can create the telephone analzer by creating a new analyzer in VisualText
# and selecting the Telephone Numbers template.

NLPPlus.set_analyzers_folder("your path to analyzers folder")
text = "My phone number is 123-456-7890. Call me at (123) 456-7890 or 123.456.7890."
results = NLPPlus.engine.analyze(text,"Telephone Numbers")
json_obj = json.loads(results.output_json)

for telephone in json_obj["telephones"]["telephone"]:
    print(f"Telephone: {telephone}")
