input_string = input()
string_list = []

for character in range(len(input_string)):
    if 65 <= ord(input_string[character]) <= 90:
        string_list.append(character)

print(string_list)



