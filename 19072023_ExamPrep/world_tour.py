def add_stop(string, current_command):
    index, string_to_add = current_command[1], current_command[2]
    index = int(index)

    if index in range(len(string)):
        string_part_1 = string[:index]
        string_part_2 = string[index:]
        string = string_part_1 + string_to_add + string_part_2

    return string


def remove_stop(string, current_command):
    start_index, end_index = current_command[1], current_command[2]
    start_index, end_index = int(start_index), int(end_index)
    if start_index in range(len(string)) and end_index in range(len(string)):
        starting_part = string[:start_index]
        ending_part = string[end_index + 1:]
        string = starting_part + ending_part

    return string


def switch(string, current_command):
    old_string, new_string = current_command[1], current_command[2]
    if old_string in string:
        string = string.replace(old_string, new_string)

    return string


input_string = input()

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        input_string = add_stop(input_string, command)
        print(input_string)
    elif action == "Remove Stop":
        input_string = remove_stop(input_string, command)
        print(input_string)
    elif action == "Switch":
        input_string = switch(input_string, command)
        print(input_string)

print(f"Ready for world tour! Planned stops: {input_string}")

