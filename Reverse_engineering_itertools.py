"""The vars function generates phonetically similar 
variations of a given word based on predefined phoneme replacements. 
It processes the input word, matches phoneme sequences 
from a dictionary (replacements), and constructs all possible phonetic variations"""

# OUTDATED !!
replacements = {
    "a": ["A"],
    "b": ["B"],
    "d": ["D"],
    "e": ["E", "É", "È", "Ê", "AI"],
    "f": ["F", "PH"],
    "i": ["I", "Y"],
    "j": ["Y"],
    "k": ["K", "C", "QU"],
    "l": ["L", "LL"],
    "m": ["M","MM"],
    "n": ["N", "NN", "NE"],
    "o": ["O", "AU", "EAU"],
    "p": ["P"],
    "r": ["R", "RR"],
    "s": ["S", "SS"],
    "t": ["T", "TT"],
    "u": ["OU"],
    "v": ["V"],
    "w": ["W"],
    "y": ["U"],
    "z": ["Z", "S"],
    "ø": ["EU", "ŒU"],
    "ŋ": ["NG"],
    "œ": ["Œ", "EU", "ŒU"],
    "œ̃": ["UN", "UM"],
    "ɑ": ["A"],
    "ɑ̃": ["AN", "AM", "EN", "EM"],
    "ɔ": ["O"],
    "ɔ̃": ["ON", "OM"],
    "ə": ["E"],
    "ɛ": ["E", "É", "È", "Ê", "AI"],
    "ɛː": ["E", "É", "È", "Ê", "AI"],
    "ɛ̃": ["IN", "IM", "AIN", "EIN"],
    "ɡ": ["G", "GU"],
    "ɥ": ["U", "HU"],
    "ɲ": ["GN"],
    "ʁ": ["R"],

    "wa": ["OIT","OI","OUA","WA","UA"],


    "ʃ": ["CH","SH"],
    "ʒ": ["J", "G", "GE"],
}


import itertools

def vars(name):
    """
    Param:
    name (str): The input word in phonetic transcription accroding to IPA convention.

    Returns:
    list: A list of possible phonetic variations.
    """
    lenname = len(name)
    incr = 0
    variations = []

    for ind in range(lenname):
        for length in range(0, lenname - incr + 1):
            substring = name[incr:lenname - length]
            if substring in replacements:
                incr += len(substring)
                
                if variations == []:
                    variations = replacements[substring]
                else:
                    variations = list(itertools.product(variations, replacements[substring]))
                    variations = [''.join(x) for x in variations]
                break #leave the loop when finding the longest variations
    return variations

"""
Remarks :
 - it iterates through the input word character by character.

 - matches the LONGEST PHONEME first (which wasn't the case with graphviz).

 - generates phonetic variations using itertools.product to create combinations of phoneme replacements."""




fr_phonemes = ['a',
 'b',
 'd',
 'e',
 'f',
 'i',
 'j',
 'k',
 'l',
 'm',
 'n',
 'o',
 'p',
 'r',
 's',
 't',
 'u',
 'v',
 'w',
 'y',
 'z',
 'ø',
 'ŋ',
 'œ',
 'œ̃',
 'ɑ',
 'ɑ̃',
 'ɔ',
 'ɔ̃',
 'ə',
 'ɛ',
 'ɛː',
 'ɛ̃',
 'ɡ',
 'ɥ',
 'ɲ',
 'ʁ',
 'ʃ',
 'ʒ',
 '‿']

import re

def trigrames_to_phoneme(text, phoneme_list):

    
    words = text.split()
    matches = []
    
    for word in words:
        for i in range(len(word) - 2):  
            substring = word[i:i+3]
            sub_transcription = model([substring], lang='fr')
            phonemes = re.findall('|'.join(map(re.escape, phoneme_list)), sub_transcription[0])
            
            if len(phonemes) == 1:  
                matches.append((substring, phonemes[0]))
    
    return matches



letters = string.ascii_lowercase  
triplets = itertools.product(letters, repeat=3)
T = []
for triplet in triplets:
    T.append(''.join(triplet))
T


S = []
for triplet in T:
    phon = model(triplet,"fr")
    if len(phon) <=1:
        S.append((triplet,phon))
S


import re
import unicodedata

def clean_text(input_str):
    """
    >>> clean_text("l'île-était très beau, même à l’été!")
    'lileetait tres beau meme a lete'
    """
    preserved = {'é', 'è', 'ê'}
    
    for char in preserved_accents:
        input_str = input_str.replace(char, f'__{char}__')
    
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    without_accents = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    without_punctuation = re.sub(r'[^\w\s]', '', without_accents)
    for char in preserved_accents:
        without_punctuation = without_punctuation.replace(f'__{char}__', char)
    
    return without_punctuation

