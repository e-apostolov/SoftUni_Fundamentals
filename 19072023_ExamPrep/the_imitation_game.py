def move(current_input, current_command):
    number_of_letters = current_command[1]
    number_of_letters = int(number_of_letters)
    part_1, part_2 = current_input[:number_of_letters], current_input[number_of_letters:]
    current_input = part_2 + part_1
    return current_input


def insert(current_input, current_command):
    index, value = current_command[1], current_command[2]
    index = int(index)
    part_1, part_2 = current_input[:index], current_input[index:]
    current_input = part_1 + value + part_2
    return current_input


def change_all(current_input, current_command):
    substring, replacement = current_command[1], current_command[2]
    current_input = current_input.replace(substring, replacement)
    return current_input


encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")
    action = command[0]

    if action == "Move":
        encrypted_message = "".join(move(encrypted_message, command))
    elif action == "Insert":
        encrypted_message = insert(encrypted_message, command)
    elif action == "ChangeAll":
        encrypted_message = change_all(encrypted_message, command)

print(f"The decrypted message is: {encrypted_message}")



