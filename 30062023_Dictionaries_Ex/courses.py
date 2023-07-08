courses_dicts = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses_dicts.keys():
        courses_dicts[course_name] = []
    courses_dicts[course_name].append(student_name)

for course, students in courses_dicts.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
