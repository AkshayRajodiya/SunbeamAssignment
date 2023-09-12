# Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube funct
# ion]
def function_cube(*args):
    list_of_cubes = []
    for values in args:
        cube = values ** 3
        list_of_cubes.append(cube)
    return list_of_cubes


result = function_cube(2, 3, 4, 5, 6)
print(result)
