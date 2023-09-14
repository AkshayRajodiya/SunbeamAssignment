# Write a method in python to display the elements of list thrice if it is a
# number and display
# the element terminated with ‘#’ if it is not a number.
# Hint-: Use InBuilt Function isdigit()
# Refer below as a input:-
# mylist = [’41’,’DROND’,’Sunbeam’, ’13’,’ZARA’]

def function(list_value):
    for values in list_value:
        if values.isdigit():
            print(f"{values * 3}")
        else:
            print(f"{'#'+values}")


mylist = ['41', 'DROND', 'Sunbeam', '13', 'ZARA']
function(mylist)
