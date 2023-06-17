string_1 = input()
string_2 = input()
last_printed_sting = string_1

for character in range(len(string_1)):
    left_part = string_2[:character + 1]
    right_part = string_1[character + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_sting:
        continue
    print(new_string)
    last_printed_sting = new_string







