def contains_substring(activation_key, some_command):
    substring = some_command[1]
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    else:
        return "Substring not found!"


def flipping(activation_key, some_command):
    upper_lower = some_command[1]
    start_index = int(some_command[2])
    end_index = int(some_command[3])
    start_substring = activation_key[:start_index]
    end_substring = activation_key[end_index:]
    substring = activation_key[start_index:end_index]
    if upper_lower == "Upper":
        substring = substring.upper()
    elif upper_lower == "Lower":
        substring = substring.lower()
    activation_key = start_substring + substring + end_substring
    return activation_key


def slicing(activation_key, some_command):
    start_index, end_index = some_command[1], some_command[2]
    start_index, end_index = int(start_index), int(end_index)
    start_substring = activation_key[:start_index]
    end_substring = activation_key[end_index:]
    activation_key = start_substring + end_substring
    return activation_key


input_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        print(contains_substring(input_activation_key, command))
    elif action == "Flip":
        input_activation_key = flipping(input_activation_key, command)
        print(input_activation_key)
    elif action == "Slice":
        input_activation_key = slicing(input_activation_key, command)
        print(input_activation_key)

print(f"Your activation key is: {input_activation_key}")

