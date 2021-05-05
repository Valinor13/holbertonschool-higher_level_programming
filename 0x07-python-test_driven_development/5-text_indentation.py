#!/usr/bin/python3
"""
A module to store simple functions for testing

...

Functions
---------
text_indentation(text)
    Prints a string of texts with new lines after '.' ':' '?'

Exceptions
----------
raise : TypeError
    Raises an error if arguments do not meet expected types
"""


def text_indentation(text):
    """A function to print a string of text with new lines
    after '.' ':' '?' and without spaces at the beginning
    of the new lines

    Parameters
    ----------
    text : str
        Input string to be parsed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    newstr = ""
    char = 0
    while char < len(text):
        if text[char] == ' ':
            while text[char + 1] == ' ':
                char += 1
        if text[char] is '.' or text[char] is '?' or text[char] is ':':
            newstr += text[char] + "\n\n"
        else:
            newstr += text[char]
        char += 1
    nustr = ""
    x = 0
    while x < len(newstr):
        if x is not len(newstr) - 1:
            if newstr[x] == '\n' and newstr[x + 1] == ' ':
                nustr += newstr[x]
                x += 1
            else:
                nustr += newstr[x]
        else:
            nustr += newstr[x]
        x += 1
    print(nustr, end="")
