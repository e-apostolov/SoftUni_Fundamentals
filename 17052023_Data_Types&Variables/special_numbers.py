# n = int(input())
# for current_number in range (1, n + 1):
#     sum_of_numbers = 0
#     digit = current_number
#     while digit > 0:
#         sum_of_numbers += digit % 10
#         digit = int(digit / 10)
#     if sum_of_numbers == 5 or sum_of_numbers == 7 or sum_of_numbers == 11:
#         print(f"{current_number} -> True")
#     else:
#         print(f"{current_number} -> False")

n = int(input())

for current_number in range(1, n +1):
    str_current_number = str(current_number)
    sum_digits = 0
    for digit in range(len(str_current_number)):
        sum_digits += int(str_current_number[digit])
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{current_number} -> True")
    else:
        print(f"{current_number} -> False")
