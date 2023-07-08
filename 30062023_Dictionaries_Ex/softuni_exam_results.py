users_max_points = {}
courses = {}

while True:
    current_results = input().split("-")

    if len(current_results) == 1:
        break
    if len(current_results) == 2:
        name = current_results[0]
        del users_max_points[name]
    elif len(current_results) == 3:
        name, course, points = current_results[0], current_results[1], int(current_results[2])

        if name not in users_max_points:
            users_max_points[name] = points
        if users_max_points[name] < points:
            users_max_points[name] = points

        if course not in courses:
            courses[course] = 0
        courses[course] += 1

print("Results:")
for key, value in users_max_points.items():
    print(f"{key} | {value}")

print("Submissions:")
for key, value in courses.items():
    print(f"{key} - {value}")





