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


# Testing
test_vig = vig("abcabc","aaa")
print(test_vig)
