# Julius Caesar Encryption Assignment
# Karl Haraldsson
# Submitted February 27, 2018

"""
Turn in the following in as homework at the beginning of class:
use remainder division to define a function Caesar (message, key) that takes a string (message) and
a number (key) as arguments and returns a string encrypted which is the result of replacing each
character in message with the letter in the alphabet that is key places to the right of it in the alphabet.
"""


alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = [",",".",";","?",":","!","$","%","&","*","(",")","/"]


def caesar(message,key):
    new_string = ""
    message_lower = message.lower()
    for i in message_lower:
        if i == " ":
            new_string += i
        elif i in punctuation:
            new_string += i
        else:
            char_index = alphabet.find(i)
            new_index = (char_index + key) % 26
            new_char = alphabet[new_index]
            new_string += new_char
    print(new_string)


testCaeasar = caesar("Be there at noon.!?",10)