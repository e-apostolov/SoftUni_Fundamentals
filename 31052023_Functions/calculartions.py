operator_input = input()
number_1 = int(input())
number_2 = int(input())

def calculator (a, b):
    if operator_input == "multiply":
        result = a * b
    elif operator_input == "divide":
        result = int(a / b)
    elif operator_input == "add":
        result = a + b
    elif operator_input == "subtract":
        result = a - b
    return result

print(calculator(number_1, number_2))

