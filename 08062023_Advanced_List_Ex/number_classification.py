# input_numbers = [int(number) for number in input().split(", ")]
# positive_numbers = [number for number in input_numbers if number >= 0]
# negative_numbers = [number for number in input_numbers if number < 0]
# odd_numbers = [number for number in input_numbers if number % 2 != 0]
# even_numbers = [number for number in input_numbers if number %2 == 0]
#
# print(f"Positive: {', '.join(map(str, positive_numbers))}")
# print(f"Negative: {', '.join(map(str, negative_numbers))}")
# print(f"Even: {', '.join(map(str, even_numbers))}")
# print(f"Odd: {', '.join(map(str, odd_numbers))}")

def positive_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if number >= 0]

def negative_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if number < 0]

def even_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if number % 2 == 0]

def odd_numbers(some_numbers: list) -> list:
    return [number for number in some_numbers if number % 2 != 0]

input_numbers = [int(number) for number in input().split(", ")]

print(f"Positive: {', '.join(map(str, positive_numbers(input_numbers)))}")
print(f"Negative: {', '.join(map(str, negative_numbers(input_numbers)))}")
print(f"Even: {', '.join(map(str, even_numbers(input_numbers)))}")
print(f"Odd: {', '.join(map(str, odd_numbers(input_numbers)))}")


