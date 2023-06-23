
initial_elements_input = [element for element in input().split()]
counter_moves  = 1

while True:
    input_indexes = input()
    if input_indexes == "end":
        if len(initial_elements_input) > 0:
            print(f"Sorry you lose :(\n"
                  f"{' '.join(initial_elements_input)}")
        break

    input_indexes = input_indexes.split()
    index_1, index_2 = int(input_indexes[0]), int(input_indexes[1])
    if index_1 == index_2 or index_1 not in range(len(initial_elements_input)) or index_2 not in range(len(initial_elements_input)):
        print("Invalid input! Adding additional elements to the board")
        initial_elements_input.insert(len(initial_elements_input)//2, f"-{counter_moves}a")
        initial_elements_input.insert(len(initial_elements_input)//2, f"-{counter_moves}a")
        continue

    if initial_elements_input[index_1] == initial_elements_input[index_2]:
        print(f"Congrats! You have found matching elements - {initial_elements_input[index_1]}!")
        if index_1 >= index_2:
            initial_elements_input.pop(index_1)
            initial_elements_input.pop(index_2)
        else:
            initial_elements_input.pop(index_2)
            initial_elements_input.pop(index_1)

    elif initial_elements_input[index_1] != initial_elements_input[index_2]:
        print("Try again!")
    if len(initial_elements_input) < 1:
        print(f"You have won in {counter_moves} turns!")
        break

    counter_moves += 1


