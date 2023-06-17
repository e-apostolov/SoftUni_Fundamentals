def sum_numbers(first, second):
    return first + second

def subtract_numbers(sum, third):
    return sum - third

def add_and_substract_numbers(number_1, number_2, number_3):
    sum_of_first_and_second_numbers = sum_numbers(number_1, number_2)
    result = subtract_numbers(sum_of_first_and_second_numbers, number_3)
    return result

first_number=int(input())
second_number=int(input())
third_number=int(input())

print(add_and_substract_numbers(first_number, second_number, third_number))

# def calculations(number_1, number_2, number_3):
#     sum_numbers = number_1 + number_2
#     result = sum_numbers - number_3
#     return result
#
#
# first_number=int(input())
# second_number=int(input())
# third_number=int(input())
#
#
# print(calculations(first_number, second_number, third_number))