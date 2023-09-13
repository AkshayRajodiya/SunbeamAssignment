# Write a program that prompts the user to input a character and determine the character is vowel or consonant.
def check_vowel_or_consonant(ch):
    list_of_vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if ch in list_of_vowels:
        print("Given character is consonant")
    else:
        print("Given character is vowel")


check_vowel_or_consonant("i")
