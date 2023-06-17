def check_palindrome(some_numbers):
    if some_numbers == some_numbers[::-1]:
        return True
    else:
        return False

input_numbers = input().split(", ")

for number in input_numbers:
    print(check_palindrome(number))