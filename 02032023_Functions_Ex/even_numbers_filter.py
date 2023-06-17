def is_even(number):
    if number % 2 == 0:
        return True
    else:
        False

input_string = input().split()
input_as_digits = []
for number in input_string:
    input_as_digits.append(int(number))

result = list(filter(is_even, input_as_digits))
print(result)


# numbers_as_string = input().split()
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
# is_even = lambda x: x % 2 == 0
# result = list(filter(is_even, numbers_as_digits))
# print(result)
#------------------------------------------------------
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         False
#
# numbers_as_string = input().split()
# numbers_as_digits = []
# for number in numbers_as_string:
#     numbers_as_digits.append(int(number))
# result = list(filter(is_even, numbers_as_digits))
# print(result)