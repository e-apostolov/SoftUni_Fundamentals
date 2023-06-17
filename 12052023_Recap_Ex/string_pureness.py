number_of_strings = int(input())

for current_string in range(number_of_strings):
    string = input()
    is_string_pure = True
    for current_character in range(len(string)):
        if string[current_character] == "," or string[current_character] == "." or string[current_character] == "_":
            is_string_pure = False
    if is_string_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")