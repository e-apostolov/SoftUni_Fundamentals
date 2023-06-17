todo_notes = [0] * 10

while True:
    note = input()
    if note == "End":
        break
    note_split = note.split("-")
    priority = int(note_split[0]) - 1
    note_text = note_split[1]
    todo_notes.pop(priority)
    todo_notes.insert(priority, note_text)

result = [notes for notes in todo_notes if notes != 0]
print(result)