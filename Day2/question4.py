# Write a program that prompts the user to input a year and determine whether the year is a leap year or
# not.
# Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100 is a leap y
# ear only if it is also evenly divisible by 400. Example :
# 1992 Leap Year
# 2000 Leap Year
# 1900 NOT a Leap Year
# 1995 NOT a Leap Year

def check_leap_year(year):
    if year % 400 == 0:
        print(f"Year is leap year : {year} ")
    elif year % 100 == 0:
        print(f"year is not leap year : {year}")
    elif year % 4 == 0:
        print(f"year is leap year : {year}")
    else:
        print(f"year is not leap year : {year}")


check_leap_year(1992)
check_leap_year(2000)
check_leap_year(1900)
check_leap_year(1995)
