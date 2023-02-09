import secrets
from math import floor
import itertools

special_characters = [
  "!", "\"", "#", "$", "%", "&", "\'", "()", "*", "+", "-", ".", "/", ":", ";",
  "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
letters_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def ask_user():
    if input("\Do you want to create a password? (y/n) ") == y:
        generate_password()