import os
from nlpengine import NLPEngine

#################################################################################
#    How to find or install the NLP engine (nlp.exe)
#
#    You can find the nlp.exe file in one of two places:
#
# 1. If you installed the NLP engine using the VisualText extension, nlp.exe is in the
#    VisualText extension directory. You can find the path to this directory by
#    going to the VisualText extension in VSCode and clicking on the three dots
#    in the top right corner of the LOGGING subpanel in the bottom panel under VISUALTEXT.
#    Then select "Engine path to clipboard". 
#
# 2. You can also clone the NLP Engine for your operation system from the GitHub. These
#    contain the nlp.exe and library files needed to run the NLP engine.
#
#    - Windows: https://github.com/VisualText/nlp-engine-windows
#    - Mac: http://github.com/VisualText/nlp-engine-mac
#    - Linux: http://github.com/VisualText/nlp-engine-linux

engineDir = "path to the nlp.exe directory"
analyzersDir = "path to your analyzers directory"
nlp = NLPEngine(engineDir,analyzersDir)

###################################################################################
# This example shows how to use the NLPEngine class to analyze text files and strings
#
# This example uses the Telephone Numbers analyzer.
# You can create the telephone analzer by creating a new analyzer in VisualText
# and selecting the Telephone Numbers template.

# Call the analyzer on a specific file that exists in the input directory
filename = "telephones.txt"
nlp.analyzeFile("Telephone Numbers", filename, True)
jsonStr = nlp.outputFileContents("Telephone Numbers", filename, "telephones.json")

# Call the analyzer on a string
filename = "tmp.txt"
telephoneStr = "My phone number is 123-456-7890. Call me at (123) 456-7890 or 123.456.7890."
nlp.analyzeStr("Telephone Numbers", filename, telephoneStr)
jsonStr = nlp.outputFileContents("Telephone Numbers", filename, "telephones.json")

print(jsonStr)