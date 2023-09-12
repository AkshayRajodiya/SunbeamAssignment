# Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit
# price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for qu
# antities over 50.
def calculate_price(quantity):
    price = 5
    if quantity < 30:
        bill_value = 5 * quantity
        return bill_value
    elif 50 > quantity > 30 :
        bill_value = (5 * quantity) - ((5 * quantity)*10/100)
        return bill_value
    else:
        bill_value = (5 * quantity) - ((5 * quantity) * 15 // 100)
        return bill_value


result = calculate_price(40)
print(result)
result_2 = calculate_price(55)
print(result_2)
result_3 = calculate_price(25)
print(result_3)

