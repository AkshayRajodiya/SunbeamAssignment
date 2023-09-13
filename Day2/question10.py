#  write a function to return compound interest. A = P(1 + R/100) t   CI = P - A
def calculate_compound_interest(principle, rate, time):
    a = principle * ((1 + rate / 100) ** time)
    compound_interest = a - principle
    return compound_interest


result = calculate_compound_interest(10000, 5, 5)
print(result)
