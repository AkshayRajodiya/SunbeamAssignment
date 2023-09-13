# Find and display the largest number of a list without using built-in function
# max(). Your program should ask the user to input values in list from keyboard.
def find_largest(length):
    list_of_ele = []

    for ele in list(range(length)):
        x = input("enter value to the list : ")
        list_of_ele.append(x)
    largest_value = list_of_ele[0]
    for value in list_of_ele:
        if value > largest_value:
            largest_value = value

    return largest_value


result = find_largest(5)
print(result)
