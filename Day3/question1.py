# Using for loop, write and run a Python program to find factorial from 0 to 10.
def find_factorial(num):
    factorial = 1
    if num < 0:
        print(" invalid input")
    elif num == 0:
        print(f"factorial of {num} is 1")
    else:
        for number in range(1, num+1):
            factorial = factorial * number

    return print(f"factorial of {num} is {factorial}")


find_factorial(0)
find_factorial(1)
find_factorial(3)
find_factorial(4)
find_factorial(5)
find_factorial(6)
find_factorial(7)
find_factorial(8)
find_factorial(9)
find_factorial(10)
