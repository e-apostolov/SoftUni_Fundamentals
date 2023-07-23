import re

title_pattern = r"<title>([^<>]*)<\/title>"
body_pattern = r"<body>.*<\/body>"
body_filtered_pattern = r">([^><]*)<"

input_line = input()

title = re.findall(title_pattern, input_line)
title = "".join(title)
print(f"Title: {title}")

body_unfiltered = re.findall(body_pattern, input_line)
body_unfiltered = "".join(body_unfiltered)

body_filtered = re.findall(body_filtered_pattern, body_unfiltered)

body_filtered = "".join(body_filtered)
body_filtered = body_filtered.replace("\\n", "")

print(f"Content: {body_filtered}")




#<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide free real-world practical\n training for young people who want to turn into\n skillful Python software engineers.</p></body>
