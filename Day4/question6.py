# Define a procedure histogram() that takes a list of integers and prints a
# histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******
def histogram(list_h):
    for value in list_h:
        print("*" * value)


histogram([4, 9, 7])