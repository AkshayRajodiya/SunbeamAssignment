# Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output = 500.
def sum_of_dictionary(dict_0):
    sum_of_values = 0
    for val in dict_0.values():
        sum_of_values += val
    return print(sum_of_values)


dict_1 = {"key_1": 200, "key": 300}
sum_of_dictionary(dict_1)
