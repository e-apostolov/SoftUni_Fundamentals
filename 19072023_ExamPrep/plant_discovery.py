def rate(plants, current_command):
    items = current_command[1].split(" - ")
    current_plant, current_rating = items[0], items[1]
    current_rating = int(current_rating)
    if current_plant not in plants:
        print("error")
        return plants
    plants_dict[current_plant][1].append(current_rating)
    return plants


def update(plants, current_command):
    items = current_command[1].split(" - ")
    current_plant, new_rarity = items[0], items[1]
    new_rarity = int(new_rarity)
    if current_plant not in plants:
        print("error")
        return plants
    plants[current_plant][0] = new_rarity
    return plants


def reset(plants, current_command):
    current_plant = current_command[1]
    if current_plant not in plants:
        print("error")
        return plants
    plants[current_plant][1] = []
    return plants


number_of_lines = int(input())
plants_dict = {}

for line in range(number_of_lines):
    current_line = input().split("<->")
    plant, rarity = current_line[0], current_line[1]
    plants_dict[plant] = [rarity, []]


while True:
    command = input()
    if command == "Exhibition":
        break
    command = command.split(": ")
    action = command[0]
    if action == "Rate":
        plants_dict = rate(plants_dict, command)
    elif action == "Update":
        plants_dict = update(plants_dict, command)
    elif action == "Reset":
        plants_dict = reset(plants_dict, command)


print("Plants for the exhibition:")
for item, value in plants_dict.items():
    total_rating = 0
    if len(value[1]) > 0:
        for rating in range(len(value[1])):
            total_rating += int(value[1][rating])
        average_rating = total_rating / (len(value[1]))
    else:
        average_rating = 0

    print(f"- {item}; Rarity: {int(value[0])}; Rating: {average_rating:.2f}")