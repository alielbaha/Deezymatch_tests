The algorithm follows these steps:
    1. Retain the first letter of the word (uppercase).
    2. Replace consonants with numeric codes based on their phonetic similarity:
       - B, F, P, V → 1
       - C, G, J, K, Q, S, X, Z → 2
       - D, T → 3
       - L → 4
       - M, N → 5
       - R → 6
    3. Remove duplicate consecutive numbers.
    4. Remove vowels (A, E, I, O, U), H, W, and Y (except for the first letter).
    5. Pad or truncate the result to ensure a 4-character code.

    Args:
        word (str): The input word to encode.

    Returns:
        str: The 4-character Soundex code.

    Example:
        >>> soundex("Robert")
        'R163'
