# Vigenere's Cypher Assignment
# Karl Haraldsson
# Due Febryary 13, 2018


def vig(s,keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = s.upper()
    keyword = keyword.upper()
    newstring = ""
    keyword_index = []
    for i in range(len(string)):
        keyword_index.append(alphabet.find(keyword[i % len(keyword)]))
    for ind in range(len(string)):
        if string[i] not in alphabet:
            newstring += string[ind]
        else:
                newstring += alphabet[(alphabet.find(string[ind]) + keyword_index[ind]) % 26]
    return newstring


"""
Create vigenere's cypher using caesar() function. Resubmitted on 11 Feb.
"""

# Include caesar cypher for use in vig_with_caesar() function
def caesar(s,k):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t = s.upper()
    newstring = ""
    for i in range(len(t)):
        if t[i] not in alphabet:
            newstring += t[i]
        else:
            newstring += alphabet[(alphabet.find(t[i]) + k) % 26]
    return newstring


# Define function vig_with_caesar() function which takes two inputs and returns encrypted text.
def vig_with_caesar(s, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = s.upper()
    keyword = keyword.upper()
    empty_string = ""
    # Loop through string and apply caesar() to each letter in string applying the key from keyword
    for i in range(len(string)):
        empty_string += str(caesar(string[i], alphabet.find(keyword[i % len(keyword)])))
    return empty_string
