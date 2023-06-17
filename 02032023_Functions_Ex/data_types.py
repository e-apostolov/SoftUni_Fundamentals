def input_processor(some_type, some_value):
    if some_type == "int":
        some_value = int(some_value)
        result = some_value * 2
    elif some_type == "real":
        some_value = float(some_value)
        result = format(some_value * 1.50, ".2f")
    elif some_type == "string":
        result = f"${some_value}$"
    return result

input_type = input()
input_value = input()

print(input_processor(input_type, input_value))