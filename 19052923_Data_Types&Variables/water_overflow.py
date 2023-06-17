number_of_lines = int(input())
remaining_capacity = 255
total_liters = 0

for pour in range(number_of_lines):
    current_pour = int(input())
    if remaining_capacity < current_pour:
        print("Insufficient capacity!")
        continue
    remaining_capacity -= current_pour
    total_liters += current_pour

print(f"{total_liters}")




