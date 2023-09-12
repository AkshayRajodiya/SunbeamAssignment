# Write a Python Program find an area of a rectangle and perimeter
# of the rectangle.

def area_and_parameter_of_rectangle(width, length):
    area = width * length
    perimeter = 2*(width + length)

    return area, perimeter


result = area_and_parameter_of_rectangle(5, 4)
print(result)
