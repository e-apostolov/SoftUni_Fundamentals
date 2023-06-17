from math import floor
def closer_to_the_centre(x1, y1, x2, y2):
    result = ()
    point_1 = (abs(x1) + abs(y1))
    point_2 = (abs(x2) + abs(y2))
    if point_1 <= point_2:
        result += floor(x1), floor(y1)
    else:
        result += floor(x2), floor(y2)
    return result

input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())

print(closer_to_the_centre(input_x1, input_y1, input_x2, input_y2))

