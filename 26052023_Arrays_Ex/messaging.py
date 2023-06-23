input_sequence_of_number = input().split()
input_string = input()
input_sequence_of_number_sum = []
input_string_str = []
print_message = []

for number in input_sequence_of_number:
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)
    input_sequence_of_number_sum.append(sum_digits)
print(input_sequence_of_number_sum)

for character in input_string:
    input_string_str.append(character)
print(input_string_str)

for letter in input_sequence_of_number_sum:
    if letter < len(input_string):
        print_message.append(input_string_str[letter])
        input_string_str.remove(input_string_str[letter])
    else:
        letter -= len(input_string)
        print_message.append(input_string_str[letter])
        input_string_str.remove(input_string_str[letter])

print(*print_message, sep="")