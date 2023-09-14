# Write a Python program to count the elements in a list until an element is a
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3
def count_ele(list_1):
    counts = 0
    for item in list_1:
        if isinstance(item, tuple):
            break
        counts += 1
    return counts


variable_list = [10, 20, 30, (40,50), 60]
print(count_ele(variable_list))