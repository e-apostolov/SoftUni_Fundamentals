number_of_entries = int(input())
all_numbers = []
filtered_numbers = []

for numbers in range(number_of_entries):
    current_number = int(input())
    all_numbers.append(current_number)

command = input()

if command == "even":
    for number in all_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == "odd":
    for number in all_numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == "negative":
    for number in all_numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == "positive":
    for number in all_numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)

