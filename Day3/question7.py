# Write a function filter_long_words() that takes a list of words and an integer
# len and returns the list of words that are longer than len.
def filter_long_words(word_list, length):

    result_word_list = []
    for words in word_list:
        word_len = len(words)
        if word_len > length:
            result_word_list.append(words)

    return result_word_list


l1 = ["i","love", "javascript", "python", "java", "c++"]
result = filter_long_words(l1,3)
print(result)