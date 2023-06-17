input_numbers = [int(number) for number in input().split(", ")]
even_number_indeces = [index for index in range(len(input_numbers)) if input_numbers[index] % 2 == 0]
print(even_number_indeces)