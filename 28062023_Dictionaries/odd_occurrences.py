input_sequence = input().split()

output_sequence = {}

for word in input_sequence:
    word_lower = word.lower()
    if word_lower not in output_sequence:
        output_sequence[word_lower] = 0
    output_sequence[word_lower] += 1

for key, value in output_sequence.items():
    if value % 2 != 0:
        print(key, end=" ")