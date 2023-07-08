input_data = input().split()

new_text = [word * len(word) for word in input_data]
print("".join(new_text))