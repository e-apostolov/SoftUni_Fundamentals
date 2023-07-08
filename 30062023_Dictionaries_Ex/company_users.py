companies_dict = {}

while True:
    command = input()
    if command == "End":
        break

    current_company, employee_ID = command.split(" -> ")

    if current_company not in companies_dict.keys():
        companies_dict[current_company] = []
    if employee_ID not in companies_dict[current_company]:
        companies_dict[current_company].append(employee_ID)

for company, ids in companies_dict.items():
    print(company)
    for employee in ids:
        print(f"-- {employee}")
