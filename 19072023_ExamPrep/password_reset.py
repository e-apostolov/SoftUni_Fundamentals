def take_odd(current_input_string):
    new_string = ""
    for index in range(len(current_input_string)):
        if index % 2 != 0:
            new_string += current_input_string[index]
    return new_string


def cut(current_input_sting, current_command):
    index, length = current_command[1], current_command[2]
    index, length = int(index), int(length)
    new_string = current_input_sting[:index] + input_string[(index+length):]
    return new_string


def substitute(current_input_string, current_command):
    substring, new_substring = current_command[1], current_command[2]
    new_string = ""
    if substring in current_input_string:
        new_string = current_input_string.replace(substring, new_substring)
    return new_string


input_string = input()

while True:
    command = input()
    if command == "Done":
        break

    command = command.split(" ")
    action = command[0]
    if action == "TakeOdd":
        input_string = take_odd(input_string)
        print(input_string)
    elif action == "Cut":
        input_string = cut(input_string, command)
        print(input_string)
    elif action == "Substitute":
        if substitute(input_string, command):
            input_string = substitute(input_string, command)
            print(input_string)
        else:
            print("Nothing to replace!")


print(f"Your password is: {input_string}")

