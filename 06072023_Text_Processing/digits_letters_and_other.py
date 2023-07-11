input_sting = input()

digits = ''
letters = ''
others = ''

for character in input_sting:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        others += character

print(digits)
print(letters)
print(others)
