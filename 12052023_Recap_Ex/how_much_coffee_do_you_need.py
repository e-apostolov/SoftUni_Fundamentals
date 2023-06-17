needed_coffee = 0
is_print_needed = True

while True:
    command = input()
    if command == "END":
        break
    if needed_coffee == 5:
        print("You need extra sleep")
        is_print_needed = False
        break
    if command == "coding" or command == "cat" or command == 'dog' or command == 'movie':
        needed_coffee += 1
    elif command == 'CODING' or command == 'CAT' or command == 'DOG' or command == 'MOVIE':
        needed_coffee += 2



if is_print_needed:
    print(f"{needed_coffee}")