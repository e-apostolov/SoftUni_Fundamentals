pair_of_entries = int(input())

student_grades_dict = {}

for index in range(pair_of_entries):
    student = input()
    grade = float(input())
    if student not in student_grades_dict:
        student_grades_dict[student] = []
    student_grades_dict[student].append(grade)

for key, value in student_grades_dict.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
