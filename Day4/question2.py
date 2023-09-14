# Write a Python Program to find the repeated item of a tuple(Take a value
# from user which you want to find)
def find_repeated(tpl_1, value):
    repeated_value = []
    for item in tpl_1:
        if item == value:
            repeated_value.append(item)

    if len(repeated_value) == 0:
        print("No repeated num")
    else:
        return print(repeated_value)


tpl_a = 11, 12, 13, 15, 17, 11, 15
find_repeated(tpl_a, 11)
