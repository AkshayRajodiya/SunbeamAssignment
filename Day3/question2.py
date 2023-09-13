# Write a program that accepts a list from user and print the alternate element
# of list.
size = int(input("Enter the size of the list :"))
list_element = []
for i in range(size):
    print(f"enter {size} values")
    x = input()
    list_element.append(x)
    size -= 1
print(list_element)
for i in range(0, len(list_element), 2):
    print(list_element[i])
