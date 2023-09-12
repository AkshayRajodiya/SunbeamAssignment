# Write a Python function to find the maximum of three numbers.
def find_max(num1, num2, num3):
    if num2 < num1 > num3:
        print("Num1 is maximum")
    elif num1 < num2 > num3:
        print("Num2 is maximum")
    else:
        print("Num3 is maximum")


find_max(1, 5, 3)
