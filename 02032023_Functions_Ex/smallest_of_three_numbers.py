def smallest_number(some_numbers):
    min_number = min(some_numbers)
    return min_number


first_number=int(input())
second_number=int(input())
third_number=int(input())

numbers = [first_number, second_number, third_number]
print(smallest_number(numbers))
