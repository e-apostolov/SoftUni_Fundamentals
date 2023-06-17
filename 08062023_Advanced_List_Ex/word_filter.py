input_list = input().split()
filtered_words = [word for word in input_list if len(word) % 2 == 0]

print("\n".join(filtered_words))