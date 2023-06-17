key = int(input())
number_of_lines = int(input())
message = ""

for characters in range(number_of_lines):
    character = input()
    character = ord(character) + key
    character = chr(character)
    message += character


print(message)


