# Write a Python Program to Convert Celsius To Fahrenheit vice
# versa.
# fahrenheit = (celsius * 1.8) + 32

def temperature_convertor(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


result = temperature_convertor(20)
print(result)
