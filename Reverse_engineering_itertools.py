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



Deux Mulets cheminaient, l’un d’avoine chargé, l’autre portant l’argent de la gabelle. Brisez les tristes fers du honteux esclavage Où vous tient du péché le commerce honteux, et venez recevoir le glorieux servage Que vous tendent les mains de la reine des cieux : L’un, sur vous, à vos sens donne pleine victoire ; l’autre sur vos désirs vous fait régner en rois ; l’un vous tire aux enfers, et l’autre dans la gloire : Hélas ! peut-on, mortels, balancer sur le choix ? Ce sont faits inouïs, grand roi, que tes victoires ! L’avenir aura peine à les bien concevoir ; et de nos vieux héros les pompeuses histoires Ne nous ont point chanté ce que tu nous fais voir. Quoi ! presque au même instant qu’on te l’a vu résoudre Voir toute une province unie à tes États ! Les rapides torrents, et les vents, et la foudre, Vont-ils, dans leurs effets, plus vite que ton bras ? N’attends pas, au retour d’un si fameux ouvrage, Des soins de notre muse un éclatant hommage. Cet exploit en demande, il le faut avouer. Mais nos chansons, grand roi, ne sont pas sitôt prêtes Et tu mets moins de temps à faire tes conquêtes Qu’il n’en faut pour les bien louer. Aux larmes, Le Vayer, laisse tes yeux ouverts : Ton deuil est raisonnable, encor qu’il soit extrême ; et, lorsque pour toujours on perd ce que tu perds, La Sagesse, crois-moi, peut pleurer elle-même. On se propose à tort cent préceptes divers Pour vouloir d’un œil sec voir mourir ce qu’on aime ; L’effort en est barbare aux yeux de l’univers, Et c’est brutalité plus que vertu suprême. On sait bien que les pleurs ne ramèneront pas Ce cher fils que t’enlève un imprévu trépas ; Mais la perte, par là, n’en est pas moins cruelle. Ses vertus de chacun le faisoient révérer ; Il avoit le cœur grand, l’esprit beau, l’âme belle ; Et ce sont des sujets à toujours le pleurer. Vous voyez bien, monsieur, que je m’écarte fort du chemin qu’on suit d’ordinaire en pareille rencontre, et que le sonnet que je vous envoie n’est rien moins qu’une consolation. Mais j’ai cru qu’il falloit en user de la sorte avec vous, et que c’est consoler un philosophe que de lui justifier ses larmes, et de mettre sa douleur en liberté. Si je n’ai pas trouvé d’assez fortes raisons pour affranchir votre tendresse des sévères leçons de la philosophie, et pour vous obliger à pleurer sans contrainte, il en faut accuser le peu d’éloquence d’un homme qui ne sauroit persuader ce qu’il sait si bien faire.
