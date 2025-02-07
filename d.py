import unicodedata
import re

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def french_soundex(word):

    word = remove_accents(word).upper()

    first_letter = word[0]
    replacements = [
        (r'[AEIOUYH]', ''),  
        (r'[BFPV]', '1'),
        (r'[CGJKQSXZ]', '2'),
        (r'[DT]', '3'),
        (r'[L]', '4'),
        (r'[MN]', '5'),
        (r'[R]', '6')
    ]

    for pattern, repl in replacements:
        word = re.sub(pattern, repl, word)

    
    word = re.sub(r'(.)\1+', r'\1', word)
    word = first_letter + word[1:]
    word = word[0] + re.sub(r'[^1-6]', '', word[1:])

    return (word + '000')[:4]
