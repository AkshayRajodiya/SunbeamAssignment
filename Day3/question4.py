# Write a program to find index of element ‘e’ in given vowels list [’a’, ’e’, ’i’,
# ’o’, ’i’, ’u’].
def find_index(ch):
    list_of_vowel = ["a", "e", "i", "o", "u"]
    return list_of_vowel.index(ch)


result = find_index("e")
print(result)
