input_string = input().split(", ")
sheep_number = 0

for sheep_index in range(len(input_string) - 1, -1, -1):
    sheep_number += 1
    if sheep_index == len(input_string) - 1 and input_string[sheep_index] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if input_string[sheep_index] == "wolf":
        print(f"Oi! Sheep number {sheep_number - 1}! You are about to be eaten by a wolf!")



