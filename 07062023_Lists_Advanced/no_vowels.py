text_input = input()
sorted_text = [letter for letter in text_input if letter.lower() not in ["a", "o", "u", "e", "i"]]

print("".join(sorted_text))