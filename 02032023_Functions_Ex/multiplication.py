# from math import prod
#
# def multiplier_check(num1, num2, num3):
#     result = ""
#     numbers = [num1, num2, num3]
#     if prod(numbers) > 0:
#         result = "positive"
#     elif prod(numbers) < 0:
#         result = "negative"
#     else:
#         result = "zero"
#     return result
#
#
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
#
# print(multiplier_check(number_1, number_2, number_3))



def multiplier_check(num1, num2, num3):
    result = ""
    multiply = num1 * num2 * num3
    if multiply > 0:
        result = "positive"
    elif multiply < 0:
        result = "negative"
    else:
        result = "zero"
    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(multiplier_check(number_1, number_2, number_3))