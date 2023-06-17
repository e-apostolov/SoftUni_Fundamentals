def sort_numbers(some_numbers):
    numbers_as_int = map(int, some_numbers)
    sorted_numbers = sorted(numbers_as_int)
    return sorted_numbers

input_numbers = input().split()
print(sort_numbers(input_numbers))