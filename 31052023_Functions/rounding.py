def round_numbers(some_numbers):
    rounded_numbers = []
    for number in some_numbers:
        rounded_numbers.append(round(float(number)))
    return rounded_numbers

input_numbers = input().split()

print(round_numbers(input_numbers))