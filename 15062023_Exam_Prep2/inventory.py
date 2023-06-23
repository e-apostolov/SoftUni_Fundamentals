def collect(some_sequence, some_item):
    if some_item not in some_sequence:
        some_sequence.append(some_item)
    return some_sequence

def drop(some_sequence, some_item):
    if some_item in some_sequence:
        some_sequence.remove(some_item)
    return some_sequence

def combine_items(some_sequence, some_items):
    old_item, new_item = some_items.split(":")
    if old_item in some_sequence:
        some_sequence.insert(some_sequence.index(old_item) + 1, new_item)
    return some_sequence

def renew(some_sequence, some_item):
    if some_item in some_sequence:
        some_sequence.append(some_sequence.pop(some_sequence.index(some_item)))
    return some_sequence


input_sequence = [word for word in input().split(", ")]

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect":
        input_sequence = collect(input_sequence, item)
    elif action == "Drop":
        input_sequence = drop(input_sequence, item)
    elif action == "Combine Items":
        input_sequence = combine_items(input_sequence, item)
    elif action == "Renew":
        input_sequence = renew(input_sequence, item)

print(", ".join(input_sequence))


