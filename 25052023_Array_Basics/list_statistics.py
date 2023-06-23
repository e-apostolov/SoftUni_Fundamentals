count_of_numbers = int(input())
positive_numbers = []
negative_numbers = []

for numbers in range(count_of_numbers):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

print(f"{positive_numbers}")
print(f"{negative_numbers}")
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")

