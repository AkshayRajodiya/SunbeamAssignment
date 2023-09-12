# Write a Python function to find the maximum of three numbers.
def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


result = find_max(12, 15, 11)
print(f"The maximum number between given number is = {result}")
result = find_max(12, 15, 19)
print(f"The maximum number between given number is = {result}")
