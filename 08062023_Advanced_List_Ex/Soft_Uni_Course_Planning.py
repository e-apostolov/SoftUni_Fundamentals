def add_lesson(some_lessons, some_title):
    if some_title not in some_lessons:
        some_lessons.append(some_title)
    return some_lessons

def insert_lesson(some_lessons, some_title, index):
    if some_title not in some_lessons:
        some_lessons.insert(index, some_title)
    return some_lessons

def remove_lesson(some_lessons, some_title):
    if some_title in some_lessons:
        title_index = some_lessons.index(some_title)
        if title_index + 1 in range(len(some_lessons)):
            if "Exercise" in some_lessons[title_index + 1]:
                some_lessons.pop(title_index + 1)
        some_lessons.remove(some_title)
    return some_lessons

def swap_lesson(some_lessons, first_lesson, second_lesson):
    if first_lesson in some_lessons and second_lesson in some_lessons:
        first_index = some_lessons.index(first_lesson)
        second_index = some_lessons.index(second_lesson)
        first_has_exercise = False
        second_has_exercise = False
        if first_index + 1 in range(len(some_lessons)):
            if "Exercise" in some_lessons[first_index + 1]:
                first_has_exercise = True
        if second_index + 1 in range(len(some_lessons)):
            if "Exercise" in some_lessons[second_index + 1]:
                second_has_exercise = True
        some_lessons[first_index], some_lessons[second_index] = some_lessons[second_index], some_lessons[first_index]
        if first_has_exercise and second_has_exercise:
            some_lessons[first_index + 1], some_lessons[second_index + 1] = some_lessons[second_index + 1], some_lessons[first_index + 1]
        elif not first_has_exercise and second_has_exercise:
            some_lessons.insert(first_index + 1, some_lessons.pop(second_index + 1))
        elif first_has_exercise and not second_has_exercise:
            some_lessons.insert(second_index + 1, some_lessons.pop(first_index + 1))
    return some_lessons

def exercise_lesson(some_lessons, some_title):
    if some_title in some_lessons and f"{some_title}-Exercise" not in some_lessons:
        title_index = some_lessons.index(some_title)
        some_lessons.insert(title_index + 1, f"{some_title}-Exercise")
    elif some_title not in some_lessons:
        some_lessons.append(some_title)
        some_lessons.append(f"{some_title}-Exercise")
    return some_lessons

lessons = input().split(", ")

while True:
    command = input().split(":")
    if len(command) < 2:
        break
    action, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    elif action == "Exercise":
        lessons = exercise_lesson(lessons,lesson_title)

for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")


