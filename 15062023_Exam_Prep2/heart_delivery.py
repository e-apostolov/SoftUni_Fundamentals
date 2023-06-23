input_string = [int(number) for number in input().split("@")]
current_index = 0

while True:
    jump_command = input()
    if jump_command == "Love!":
        break
    jump_command = jump_command.split()
    jump_lenght = int(jump_command[1])

    if current_index + jump_lenght >= len(input_string):
        current_index = 0
        if input_string[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
            continue
        input_string[current_index] -= 2
        if input_string[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    else:
        current_index += jump_lenght
        if input_string[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
            continue
        input_string[current_index] -= 2
        if input_string[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

print(f"Cupid's last position was {current_index}.")
final_string = [number for number in input_string if number != 0]

if len(final_string) > 0:
    print(f"Cupid has failed {len(final_string)} places.")
else:
    print(f"Mission was successful.")




