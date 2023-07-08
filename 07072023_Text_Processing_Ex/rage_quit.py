input_sequence = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ""

for index in range(len(input_sequence)):

    if not input_sequence[index].isdigit():
        current_symbol += input_sequence[index]

    else:
        for next_symbols in range(index, len(input_sequence)):
            if not input_sequence[next_symbols].isdigit():
                break
            else:
                repetitions += input_sequence[next_symbols]

        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(f"{unique_symbols}")

