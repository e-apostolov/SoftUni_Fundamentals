input_numbers = input().split()
numbers_to_remove = int(input())
input_numbers_int = []

for number in input_numbers:
    input_numbers_int.append(int(number))

input_numbers_int.sort()
for number in range(numbers_to_remove):
    input_numbers.remove(str(input_numbers_int[number]))

print(*input_numbers, sep=", ")

