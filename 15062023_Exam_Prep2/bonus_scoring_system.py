from math import ceil

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
students_attendance = []

for student in range(number_of_students):
    students_attendance.append(int(input()))

if total_number_of_lectures != 0:
    print(f"Max Bonus: {ceil(max(students_attendance) / total_number_of_lectures * (5  + additional_bonus))}.")
    print(f"The student has attended {max(students_attendance):.0f} lectures.")

else:
    print(f"Max Bonus: {0}.")
    print(f"The student has attended {0} lectures.")


# number_of_students = int(input())
# total_number_of_lectures = int(input())
# additional_bonus = int(input())
# current_max_bonus = 0
# max_student_index = 0
# student_max_attendance = 0
#
# for student in range(number_of_students):
#     student_attendence = int(input())
#     student_bonus = student_attendence / total_number_of_lectures * (5 + additional_bonus)
#     if student_bonus > current_max_bonus:
#         current_max_bonus = student_bonus
#         max_student_index = student_bonus
#         student_max_attendance = student_attendence
#
#
#
# print(f"Max Bonus: {current_max_bonus:.0f}.")
# print(f"The student has attended {student_max_attendance:.0f} lectures.")