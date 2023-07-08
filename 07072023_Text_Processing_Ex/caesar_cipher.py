input_sequence = input()
output_sequence = ""

for character in input_sequence:
    new_character = chr(ord(character) + 3)
    output_sequence += new_character

print(output_sequence)