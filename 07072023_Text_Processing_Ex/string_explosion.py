input_string = input()
output_string = ""
strength = 0

for index in range(len(input_string)):

    if strength > 0 and input_string[index] != ">":
        strength -= 1

    elif input_string[index] == ">":
        output_string += input_string[index]
        strength += int(input_string[index + 1])

    else:
        output_string += input_string[index]


print(output_string)