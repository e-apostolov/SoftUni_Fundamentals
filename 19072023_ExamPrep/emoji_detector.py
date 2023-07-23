import re

input_string = input()

pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
numbers_pattern = r"\d"

matches = re.findall(pattern, input_string)
numbers_matches = re.findall(numbers_pattern, input_string)
cool_threshold = 1
for number in numbers_matches:
    cool_threshold *= int(number)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(list(matches))} emojis found in the text. The cool ones are:")

for match in matches:
    match_sum = 0
    for char in match[1]:
        match_sum += ord(char)
    if match_sum > cool_threshold:
        print("".join(match))


