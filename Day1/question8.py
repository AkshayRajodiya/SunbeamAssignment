# Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
calculate_number_of_calls = int(input("Enter number of calls :"))
x = 0
y = 0
z = 0
if calculate_number_of_calls <= 100:
    bill_value = 200
    print(f"bill is {bill_value} Rs")
elif 100 < calculate_number_of_calls <= 150:
    x = calculate_number_of_calls - 100
    bill_value = (x * 0.6) + 200
    print(f"bill is {bill_value} Rs")
elif 150 < calculate_number_of_calls <= 200:
    y = calculate_number_of_calls - 150
    bill_value = (y * 0.5) + (50 * 0.6) + 200
    print(f"bill is {bill_value} Rs")
else:
    z = calculate_number_of_calls - 200
    bill_value = (z * 0.4) + (50 * 0.5) + (50 * 0.6) + 200
    print(f"bill is {bill_value} Rs")
