import re

input_sentence = input()
search_word = input()

pattern = fr"\b{search_word}\b"

matches = re.findall(pattern, input_sentence, re.IGNORECASE)

print(len(matches))
