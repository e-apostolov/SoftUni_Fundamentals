input_numbers = [int(number) for number in input().split(", ")]
current_group_of_numbers = 10

while input_numbers:
    filtered_numbers = [number for number in input_numbers if number <= current_group_of_numbers]
    print(f"Group of {current_group_of_numbers}'s: {filtered_numbers}")
    current_group_of_numbers += 10
    input_numbers = [s for s in input_numbers if s not in filtered_numbers]

