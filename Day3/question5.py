# Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise.
def function_overlapping(list_1, list_2):
    for ele in list_1:
        for val in list_2:
            if ele == val:
                return True

    return False


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = [11, 23, 32, 43, 1]
result = function_overlapping(l1, l2)
result_1 = function_overlapping(l1, l3)
print(result)
print(result_1)
