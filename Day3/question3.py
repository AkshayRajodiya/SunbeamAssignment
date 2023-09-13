# Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3].
def replace_value(list_1, list_2):
    given_list = list_1
    for values in given_list:
        if values == "b":
            index = given_list.index('b')
            given_list.remove("b")
            given_list.insert(index, list_2)

    return given_list


l1 = ["a", "b", "c", "d", "e"]
l2 = [1, 2, 3]
result = replace_value(l1, l2)
print(result)
