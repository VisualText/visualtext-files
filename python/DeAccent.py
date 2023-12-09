# Deacent words in the current text

import sys

from unidecode import unidecode

file_path = sys.argv[1]

with open(file_path, encoding='utf8') as f:
    file_text = f.read()
    
text_without_accents = unidecode(file_text)

print(text_without_accents)