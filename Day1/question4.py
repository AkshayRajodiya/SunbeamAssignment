# Write a program to accept three integer numbers and find its
# average.
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))
average = (num1 + num2 + num3) / 3
print(f"the average of given numbers is {average}")


# using function.
def average(v1, v2, v3):

    return (v1+v2+v3)//3


result = average(12, 13, 14)
print(result)
