factor_number = int(input())
count_number = int(input())
output_list = []

for number in range(1, count_number + 1):
    output_list.append(number * factor_number)

print(output_list)
