# input_number = int(input())
# input_number_str = str(input_number)
#
# for highest_number in range (9, -1, -1):
#     for digit in input_number_str:
#         if highest_number == int(digit):
#             print(highest_number, end="")


input_number = int(input())
input_number_str = str(input_number)

for highest_number in range(9, -1, -1):
    for digit in range(len(input_number_str)):
        if highest_number == int(input_number_str[digit]):
            print(highest_number, end="")