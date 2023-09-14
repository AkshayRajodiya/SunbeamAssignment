# Concatenate two lists in the following order by using list comprehension
# Input:- list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Output:- [’Hello Dear’, ’Hello Sir’, ’take Dear’, ’take Sir’]

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [string_1 + string_2 for string_1 in list1 for string_2 in list2 ]
print(result)
