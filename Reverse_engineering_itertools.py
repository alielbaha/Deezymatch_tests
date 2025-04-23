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


arabic_string = 'ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ء أ إ آ ى ة ئ ؤ'

phoneme_symbols: ['p', 'b', 't', 'd', 'ʈ', 'ɖ', 'c', 'ɟ', 'k', 'ɡ', 'q', 'ɢ', 'ʡ', 'ʔ', 'm', 'ɱ', 'n', 'ɳ', 'ɲ', 'ŋ', 'ɴ', 'ʙ', 'r', 'ʀ', 'ɾ', 'ɽ', 'ɸ', 'β', 'f', 'v', 'θ', 'ð', 's', 'z', 'ʃ', 'ʒ', 'ʂ', 'ʐ', 'ç', 'ʝ', 'x', 'ɣ', 'χ', 'ʁ', 'ħ', 'ʕ', 'h', 'ɦ', 'ɬ', 'ɮ', 'ʋ', 'ɹ', 'ɻ', 'j', 'ɰ', 'l', 'ɭ', 'ʎ', 'ʟ', 'i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'ə', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ɑ', 'ɒ', 'ʘ', 'ǀ', 'ǃ', 'ǂ', 'ǁ', 'ɓ', 'ɗ', 'ʄ', 'ɠ', 'ʛ', 'ˈ', 'ˌ', '.', 'ː', 'ˑ', '|', '‖', 'ʍ', 'w', 'ɥ', '̃', '̥', '̬', '̹', '̜', '̟', '̠', '̈', '̽', '̩', '̯', 'ʰ', 'ʲ', '˞', 'ⁿ', 'ˠ']

import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter

# Your replacement dictionary (example)
replacements = {
    "br": ["br", "pr"],
    "u": ["u", "oo", "ou"],
    "ce": ["ce", "s", "se"],
    "oo": ["u", "ou"],
    "ph": ["f", "v"],
    "sh": ["ch", "s"]
}

# Modified vars function
def vars(name, replacements):
    lenname = len(name)
    incr = 0
    variations = []
    substitution_count = 0
    replaced_substrings = []

    for ind in range(lenname):
        for length in range(0, lenname - incr + 1):
            substring = name[incr:lenname - length]
            if substring in replacements:
                incr += len(substring)
                substitution_count += 1
                replaced_substrings.append(substring)
                if not variations:
                    variations = replacements[substring]
                else:
                    variations = list(itertools.product(variations, replacements[substring]))
                    variations = [''.join(x) for x in variations]
                break

    return {
        "original": name,
        "variations": variations,
        "variation_count": len(variations),
        "substitution_count": substitution_count,
        "replaced_substrings": replaced_substrings
    }

--------------------


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Replacement rules and variation generator (from previous solution)
replacements = {
    "ɛː": ["E", "É", "È", "Ê", "AI"],
    "ɛ̃": ["IN", "IM", "AIN", "EIN"],
    "w": ["G", "GU"],
    "ɥ": ["U", "HU"],
    "ɲ": ["GN"],
    "ʁ": ["R"],
    "wa": ["OIT", "OI", "OUA", "WA", "UA"],
}

def vars(name):
    def helper(s):
        if not s:
            return ['']
        results = []
        max_len = min(len(s), max(len(k) for k in replacements))
        for l in range(max_len, 0, -1):
            prefix = s[:l]
            if prefix in replacements:
                for replacement in replacements[prefix]:
                    for suffix_variation in helper(s[l:]):
                        results.append(replacement + suffix_variation)
        if not results:
            first_char = s[0]
            for suffix_variation in helper(s[1:]):
                results.append(first_char + suffix_variation)
        return results
    return helper(name)

# Example names for analysis (replace with your dataset)
sample_names = [
    "wa",       # Example with multi-character key "wa" and single "w"
    "wɥ",       # Example with two single-character keys ("w" and "ɥ")
    "ɲa",       # Example with one replacement ("ɲ") and no replacement ("a")
    "ɛːwa",     # Combines "ɛː" and "wa"
    "ʁɥ",       # Two single-character replacements
    "test",     # No replacements (original string returned)
    "ɛ̃ɲʁ"       # Multiple single-character replacements
]

# Generate variation counts for each name
variation_counts = []
for name in sample_names:
    variations = vars(name)
    variation_counts.append({
        "name": name,
        "variation_count": len(variations),
        "variations": variations
    })

# Create DataFrame for analysis
df = pd.DataFrame(variation_counts)

# Basic statistics
total_names = df.shape[0]
total_variations = df["variation_count"].sum()
stats = {
    "Total Names": total_names,
    "Total Variations": total_variations,
    "Min Variations": df["variation_count"].min(),
    "Max Variations": df["variation_count"].max(),
    "Mean Variations": df["variation_count"].mean(),
    "Median Variations": df["variation_count"].median(),
    "Std Dev Variations": df["variation_count"].std()
}

# Display statistics
print("=== Summary Statistics ===")
for key, value in stats.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

# Plot distribution of variation counts
plt.figure(figsize=(10, 6))
plt.hist(df["variation_count"], bins=np.arange(0.5, df['variation_count'].max() + 1, 1), edgecolor='black')
plt.title("Distribution of Variation Counts per Name")
plt.xlabel("Number of Variations")
plt.ylabel("Frequency")
plt.xticks(range(1, df['variation_count'].max() + 1))
plt.grid(axis='y', alpha=0.75)
plt.show()

# Show names with extremes (min/max variations)
print("\n=== Names with Minimum Variations ===")
print(df[df["variation_count"] == df["variation_count"].min()][["name", "variation_count"]])

print("\n=== Names with Maximum Variations ===")
print(df[df["variation_count"] == df["variation_count"].max()][["name", "variation_count"]])
