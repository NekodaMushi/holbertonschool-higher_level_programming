#!/usr/bin/python3
"""prints a text with 2 new lines"""


def text_indentation(text):
    """Prints after each of these characters: 
    . , ? and :

    Raise exception if text is not a string

    Returns: Nothing

    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(f"{text[i]}", end="")
            i += 1
