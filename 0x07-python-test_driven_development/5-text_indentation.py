#!/usr/bin/python3
""" """


def text_indentation(text):
    """ """

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
        if newstr[x] == '\n' and newstr[x + 1] == ' ':
            nustr += newstr[x]
            x += 1
        else:
            nustr += newstr[x]
        x += 1
    print(nustr)
