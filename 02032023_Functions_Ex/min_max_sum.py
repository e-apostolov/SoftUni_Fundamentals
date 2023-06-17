def combined_calculation(some_numbers):
    numbers_as_int = list(map(int, some_numbers))
    min_number = min(numbers_as_int)
    max_number = max(numbers_as_int)
    sum_numbers = sum(numbers_as_int)
    result = (f"The minimum number is {min_number}\n"
              f"The maximum number is {max_number}\n"
              f"The sum number is: {sum_numbers}")
    return result


input_numbers = input().split()
print(combined_calculation(input_numbers))