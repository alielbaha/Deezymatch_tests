A simplified version of the Double Metaphone algorithm.

    This function takes an English word and generates two phonetic keys:
    - Primary Key: Represents the most common pronunciation.
    - Secondary Key: Accounts for alternative pronunciations.

    The algorithm follows these rules:
    1. Handles silent letters at the start (e.g., "KN" → "N", "WR" → "R").
    2. Replaces letter patterns with their phonetic equivalents (e.g., "PH" → "F").
    3. Simplifies complex consonant sounds (e.g., "SCH" → "SK").
    4. Removes certain trailing letters (e.g., "Y" and "W" at the end of words).
    5. Generates a secondary key with slight variations for alternate pronunciations.

    Args:
        word (str): The input word to be processed.

    Returns:
        tuple: A pair of strings representing the primary and secondary phonetic keys.

    Example:
        >>> simple_double_metaphone("knight")
        ('NIGT', 'NIGT')

        >>> simple_double_metaphone("xylophone")
        ('KSLOFONE', 'XSLOFONE')
    """
