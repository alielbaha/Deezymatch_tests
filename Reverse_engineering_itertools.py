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




Ceux qui vivent, ce sont ceux qui luttent ; ce sont Ceux dont un dessein ferme emplit l’âme et le front, Ceux qui d’un haut destin gravissent l’âpre 1  cime, Ceux qui marchent pensifs, épris d’un but sublime, Ayant devant les yeux sans cesse, nuit et jour, Ou quelque saint labeur ou quelque grand amour. C’est 2  le prophète saint prosterné devant l’arche, C’est le travailleur, pâtre, ouvrier, patriarche ; Ceux dont le cœur est bon, ceux dont les jours sont pleins, Ceux-là vivent, Seigneur ! les autres, je les plains. Car de son vague ennui le néant 3  les enivre, Car le plus lourd fardeau, c’est d’exister sans vivre. Inutiles, épars, ils traînent ici-bas Le sombre accablement d’être en ne pensant pas. Ils s’appellent vulgus, plebs, la tourbe, la foule. Ils sont ce qui murmure, applaudit, siffle, coule, Bat des mains, foule aux pieds, bâille, dit oui, dit non, N’a jamais de figure et n’a jamais de nom ; Troupeau qui va, revient, 4  juge, absout, délibère, Détruit, prêt à Marat comme prêt à Tibère, Foule triste, joyeuse, habits dorés, bras nus, Pêle-mêle, et poussée aux gouffres inconnus. Ils sont les passants froids, sans but, sans 5  nœud, sans âge ; Le bas du genre humain qui s’écroule en nuage ; Ceux qu’on ne connaît pas, ceux qu’on ne compte pas, Ceux 6  qui perdent les mots, les volontés, les pas. L’ombre obscure autour d’eux se prolonge et recule ; Ils n’ont du plein midi qu’un lointain crépuscule, Car, jetant au 7  hasard les cris, les voix, le bruit, Ils errent près du bord sinistre de la nuit. Quoi, ne point aimer ! suivre une morne carrière, Sans un songe en avant, sans un deuil en arrière ! Quoi ! marcher devant 8  soi sans savoir où l’on va ! Rire de Jupiter sans croire à Jéhova ! Regarder sans respect l’astre, la fleur, la femme ! Toujours vouloir le corps, ne jamais chercher 9  l’âme ! Pour de vains résultats faire de vains efforts ! N’attendre rien d’en haut ! ciel ! oublier les morts ! Oh non, je ne suis point de ceux-là ! grands, prospères, Fiers, puissants, ou cachés dans d’immondes repaires, Je les fuis, et je crains leurs sentiers détestés ; Et j’aimerais mieux 10  être, ô fourmis des cités, Tourbe, foule, hommes faux, cœurs morts, races déchues Un arbre dans les bois qu’une âme en vos cohues
