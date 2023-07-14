input_lines = int(input())

for command in range(input_lines):

    current_command = input()
    name_start_index = 0
    name_end_index = 0
    age_start_index = 0
    age_end_index = 0

    for index in range(len(current_command)):
        if current_command[index] == "@":
            name_start_index = index
        elif current_command[index] == "|":
            name_end_index = index
        elif current_command[index] == "#":
            age_start_index = index
        elif current_command[index] == "*":
            age_end_index = index

    name = current_command[(name_start_index + 1):name_end_index]
    age = current_command[(age_start_index + 1):age_end_index]

    print(f"{name} is {age} years old.")





