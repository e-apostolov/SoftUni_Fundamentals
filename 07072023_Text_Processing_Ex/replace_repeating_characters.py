input_string = input()
output_string = ""
last_character = ""

for char in input_string:
    if char != last_character:
        output_string += char
        last_character = char

print(output_string)
