# def check_employee_happiness():
#     happiness_list = list(map(int, input().split(" ")))
#     happiness_factor = int(input())
#
#     improve_happiness = [h * happiness_factor for h in happiness_list]
#
#     average_happiness = sum(improve_happiness) / len(improve_happiness)
#     happy_count = sum(h >= average_happiness for h in improve_happiness)
#
#     total_count = len(improve_happiness)
#     message = "happy" if happy_count >= total_count / 2 else "not happy"
#     result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
#
#     return result
#
# result = check_employee_happiness()
# print(result)


employees = input().split(" ")
employees_numbers = list(map(int,employees))
happiness_factor = int(input())

def happiness_checker(some_emplyees, some_factor):
    improved_happiness = [h * some_factor for h in some_emplyees]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(h >= average_happiness for h in improved_happiness)
    if happy_count >= len(improved_happiness) / 2:
        result = f"Score: {happy_count}/{len(improved_happiness)}. Employees are happy!"
    else:
        result = f"Score: {happy_count}/{len(improved_happiness)}. Employees are not happy!"
    return result

print(happiness_checker(employees_numbers, happiness_factor))

