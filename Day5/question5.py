# Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

def find_odd_even(li):
    even = []
    odd = []
    result = {}
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result["Even"] = even
    result["Odd"] = odd
    print(result)


find_odd_even([1,5,8,9,10,64])