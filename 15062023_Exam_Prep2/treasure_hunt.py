def command_loot (some_loot, some_command):
    some_items = some_command[1:]
    for item in some_items:
        if item not in some_loot:
            some_loot.insert(0, item)
    return some_loot

def command_drop (some_loot, some_command):
    some_index = int(some_command[1])
    if some_index in range(len(some_loot)):
        some_loot.append(some_loot.pop(some_index))
    return some_loot

def command_steal (some_loot, some_command):
    some_index = some_command[1]
    if len(some_loot) > int(some_index):
        items_to_remove = len(some_loot) - int(some_index)
        stolen_loot = some_loot[items_to_remove:]
        some_loot = some_loot[:items_to_remove]
        print(", ".join(stolen_loot))
    else:
        print(", ".join(some_loot))
        some_loot = []
    return some_loot

initial_loot = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break
    command = command.split()
    if command[0] == "Loot":
        initial_loot = command_loot(initial_loot, command)
    elif command[0] == "Drop":
        initial_loot = command_drop(initial_loot, command)
    elif command[0] == "Steal":
        initial_loot = command_steal(initial_loot, command)


if len(initial_loot) > 0:
    average_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")


