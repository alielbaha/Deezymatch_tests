import re

def metaphone(word):
    """
    args:
        str: The input word to be processed

    returns:
        str: The phonetic representation of the word

    examples:
        >>> metaphone("knight")
        'NIGT'

        >>> metaphone("michael")
        'MKL'
    """
    word = word.upper()
    word = re.sub(r'[^A-Z]', '', word)  
    
    
    if word.startswith("KN") or word.startswith("GN") or word.startswith("PN") or word.startswith("WR") or word.startswith("PS"):
        word = word[1:]
    
    result = ""
    previous_char = ""
    
    i = 0
    while i < len(word):
        char = word[i]
        
        if char == previous_char:
            i += 1
            continue
        
        if char in "AEIOU" and i == 0:
            result += char
        elif char in "BFPV":
            result += "F"
        elif char in "CKQ":
            result += "K"
        elif char == "G":
            if (i < len(word) - 1 and word[i + 1] == "H") or (i > 0 and word[i - 1] in "G"):  # silent G
                pass
            elif i < len(word) - 2 and word[i + 1] in "IEY":
                result += "J"
            else:
                result += "K"
        elif char == "H":
            if i > 0 and word[i - 1] in "AEIOU":
                result += "H"
        elif char == "J":
            result += "J"
        elif char == "L":
            result += "L"
        elif char == "M" or char == "N":
            result += char
        elif char == "R":
            result += "R"
        elif char in "SZ":
            result += "S"
        elif char == "T":
            if i < len(word) - 2 and word[i + 1:i + 3] == "CH":
                pass
            else:
                result += "T"
        elif char in "DT":
            result += "T"
        elif char == "V":
            result += "F"
        elif char == "W" or char == "Y":
            if i < len(word) - 1 and word[i + 1] in "AEIOU":
                result += char
        elif char == "X":
            result += "KS"
        
        previous_char = char
        i += 1
    
    return result
