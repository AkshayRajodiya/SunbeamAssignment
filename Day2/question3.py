# write a program to find given number is positive ,negative or zero.
def find_type_of_number(num):
    if num > 0:
        print("Given number is positive")
    elif num < 0:
        print("Given number is negative")
    elif num == 0:
        print("Given number is zero")
    else:
        print("Invalid input")


find_type_of_number(5)
