input_string = input().split(", ")
number_of_beggers = int(input())
input_string_int = []

for element in input_string:
    input_string_int.append(int(element))

final_sums = []
start_index = 0

while start_index < number_of_beggers:
    sum_for_current_begger = 0
    for current_index in range(start_index, len(input_string_int), number_of_beggers):
        sum_for_current_begger += input_string_int[current_index]
    final_sums.append(sum_for_current_begger)
    start_index += 1

print(final_sums)




