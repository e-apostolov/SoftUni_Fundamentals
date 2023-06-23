first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
hours_count = 0
total_time = 0

total_efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

while students_count > 0:
    hours_count += 1
    total_time += 1
    if hours_count % 4 == 0:
        continue
    students_count -= total_efficiency_per_hour

print(f"Time needed: {hours_count}h.")

