# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
def calculate_telephone_bill(value):
    x = 0                              # extra charge for 100-150.
    y = 0                              # extra charge for 150-200.
    z = 0                              # extra charge after 200.
    if value <= 100:
        bill_value = 200
        print(f"bill is {bill_value} Rs")
    elif 100 < value <= 150:
        x = value - 100
        bill_value = (x * 0.6) + 200
        print(f"bill is {bill_value} Rs")
    elif 150 < value <= 200:
        y = value - 150
        bill_value = (y * 0.5) + (50 * 0.6) + 200
        print(f"bill is {bill_value} Rs")
    else:
        z = value - 200
        bill_value = (z * 0.4) + (50 * 0.5) + (50 * 0.6) + 200
        print(f"bill is {bill_value} Rs")


calculate_telephone_bill(100)
calculate_telephone_bill(110)
calculate_telephone_bill(160)
calculate_telephone_bill(201)