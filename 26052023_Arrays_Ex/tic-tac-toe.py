array_sequence = []

for n in range(3):
    input_sequence = input().split(" ")
    array_sequence.append(input_sequence)

winner = 0

for options in range(1, 3):
    if array_sequence[0][0] == array_sequence[0][1] == array_sequence[0][2] == str(options) or \
            array_sequence[1][0] == array_sequence[1][1] == array_sequence[1][2] == str(options) or \
            array_sequence[2][0] == array_sequence[2][1] == array_sequence[2][2] == str(options):
        winner = options
    elif array_sequence[0][0] == array_sequence[1][0] == array_sequence[2][0] == str(options) or \
            array_sequence[0][1] == array_sequence[1][1] == array_sequence[2][1] == str(options) or \
            array_sequence[0][2] == array_sequence[1][2] == array_sequence[2][2] == str(options):
        winner = options
    elif array_sequence[0][0] == array_sequence[1][1] == array_sequence[2][2] == str(options) or \
            array_sequence[0][2] == array_sequence[1][1] == array_sequence[2][0] == str(options):
        winner = options

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")


