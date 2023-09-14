# Write a function find_longest_word() that takes a list of words and returns
# the length of the longest
# one.
def find_longest_word(w_list):
    count = 0
    longest_word = ""
    for word in w_list:
        length_of_word = len(word)
        if length_of_word > count:
            count = len(word)
            longest_word = word
    return count, longest_word


print(find_longest_word(["i", "love", "javaScript", "python"]))
