# write a function to return simple interest.
def simple_interest(principle, rate, time):
    result = (principle * rate * time) / 100
    return result


value = simple_interest(10000, 5, 1)
print(value)
