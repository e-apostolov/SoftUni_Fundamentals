while True:

    input_string = input()
    new_input_string = ""
    if input_string == "End":
        break
    if input_string == "SoftUni":
        continue
    for i in range(len(input_string)):
        new_input_string += 2 * input_string[i]
    print(new_input_string)

