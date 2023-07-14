import re

pattern = r"((w{3}\.[a-zA-Z0-9-]+)(\.[a-z]+)+)"

line = input()

while line:
    matches = re.search(pattern, line)
    if matches:
        print(matches.group(0))
    line = input()

