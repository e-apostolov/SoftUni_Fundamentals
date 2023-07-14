import re

input_sentence = input()

pattern = r"\b_([a-zA-Z0-9]+)\b"

matches = re.findall(pattern, input_sentence)

print(",".join(matches))