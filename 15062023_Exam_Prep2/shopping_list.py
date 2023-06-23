def urgent(some_shopping_list, some_item):
    if some_item not in some_shopping_list:
        some_shopping_list.insert(0, some_item)
    return some_shopping_list

def unnecassary(some_shopping_list, some_item):
    if some_item in some_shopping_list:
        some_shopping_list.remove(some_item)
    return some_shopping_list

def correct(some_shopping_list, old_item, new_item):
    if old_item in some_shopping_list:
        some_shopping_list[some_shopping_list.index(old_item)] = new_item
    return some_shopping_list

def rearrange(some_shopping_list, some_item):
    if some_item in some_shopping_list:
        some_shopping_list.append(some_shopping_list.pop(some_shopping_list.index(some_item)))
    return some_shopping_list


initial_shopping_list = [item for item in input().split("!")]

while True:
    command = input()
    if command == "Go Shopping!":
        break
    command = command.split()
    action = command[0]
    item = command[1]
    if len(command) > 2:
        item_2 = command[2]

    if action == "Urgent":
        initial_shopping_list = urgent(initial_shopping_list, item)
    elif action == "Unnecessary":
        initial_shopping_list = unnecassary(initial_shopping_list, item)
    elif action == "Correct":
        initial_shopping_list = correct(initial_shopping_list, item, item_2)
    elif action == "Rearrange":
        initial_shopping_list = rearrange(initial_shopping_list, item)

print(", ".join(initial_shopping_list))


