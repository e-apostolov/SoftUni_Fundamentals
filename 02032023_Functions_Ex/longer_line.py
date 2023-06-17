from math import floor
def longest_line(x1, y1, x2, y2, x3, y3, x4, y4):
    result = ""
    point_1 = abs(x1) + abs(y1)
    point_2 = abs(x2) + abs(y2)
    point_3 = abs(x3) + abs(y3)
    point_4 = abs(x4) + abs(y4)
    line_1_lenght = point_1 + point_2
    line_2_lenght = point_3 + point_4
    x1, y1, x2, y2, x3, y3, x4, y4 = floor(x1), floor(y1), floor(x2), floor(y2), floor(x3), floor(y3), floor(x4), floor(y4)
    if line_1_lenght >= line_2_lenght:
        if point_1 <= point_2:
            result = f"({x1}, {y1})({x2}, {y2})"
        else:
            result = f"({x2}, {y2})({x1}, {y1})"
    else:
        if point_3 <= point_4:
            result = f"({x3}, {y3})({x4}, {y4})"
        else:
            result = f"({x4}, {y4})({x3}, {y3})"
    return result

input_x1 = float(input())
input_y1 = float(input())
input_x2 = float(input())
input_y2 = float(input())
input_x3 = float(input())
input_y3 = float(input())
input_x4 = float(input())
input_y4 = float(input())

print(longest_line(input_x1, input_y1, input_x2, input_y2, input_x3, input_y3, input_x4, input_y4))

