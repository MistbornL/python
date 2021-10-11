'''The Atbash cipher is an encryption method in which each letter
of a word is replaced with its "mirror" letter in the alphabet: A
<=> Z; B <=> Y; C <=> X; etc.
Create a function that takes a string and applies the Atbash cipher to it.


atbash("apple") ➞ "zkkov"


atbash("Hello world!") ➞ "Svool dliow!"


atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"'''
from string import  ascii_lowercase

def atbash(x):
    my_string = ""
    for letter in x.lower():
        if letter.isdigit():
            my_string += letter
        elif letter in '!@#$%^&*()_+,./; ':
            my_string += letter
        else:
            index = ascii_lowercase.index(letter) + 1
            my_string += ascii_lowercase[-index]
    print(f"{x} => {my_string}")    
atbash("Christmas is the 25th of December")