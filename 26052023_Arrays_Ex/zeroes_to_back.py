input_string = input().split(", ")
input_string_int = []
for number in input_string:
    input_string_int.append(int(number))

for element in input_string_int:
    if element == 0:
        input_string_int.remove(element)
        input_string_int.append(element)

print(input_string_int)
