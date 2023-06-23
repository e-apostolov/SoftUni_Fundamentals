def swap(some_numbers, index1, index2):
    some_numbers[index1], some_numbers[index2] = some_numbers[index2], some_numbers[index1]
    return some_numbers

def multiply(some_numbers, index1, index2):
    some_numbers[index1] *= some_numbers[index2]
    return some_numbers

def decrase(some_numbers):
    for multiplayer in range(len(some_numbers)):
        some_numbers[multiplayer] -= 1
    return some_numbers

input_numbers = [int(number) for number in input().split()]

while True:
    command = input()
    if command == "end":
        break
    elif command == "decrease":
        input_numbers = decrase(input_numbers)
    command = command.split()
    action = command[0]
    if len(command) > 1:
        index_1 = int(command[1])
        index_2 = int(command[2])
    if action == "swap":
        input_numbers = swap(input_numbers, index_1, index_2)
    elif action == "multiply":
        input_numbers = multiply(input_numbers, index_1, index_2)

print(*input_numbers, sep=", ")

