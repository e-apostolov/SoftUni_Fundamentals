number_of_dragons = int(input())
dragons_dict = {}

for dragon in range(number_of_dragons):
    dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = input().split()
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    dragon_damage, dragon_health, dragon_armor = int(dragon_damage), int(dragon_health), int(dragon_armor)

    if dragon_type not in dragons_dict:
        dragons_dict[dragon_type] = {dragon_name: [dragon_damage, dragon_health, dragon_armor]}

    elif dragon_type in dragons_dict:
        if dragon_name not in dragons_dict[dragon_type]:
            dragons_dict[dragon_type].update({dragon_name: [dragon_damage, dragon_health, dragon_armor]})
        elif dragon_name in dragons_dict[dragon_type]:
            dragons_dict[dragon_type][dragon_name][0] = dragon_damage
            dragons_dict[dragon_type][dragon_name][1] = dragon_health
            dragons_dict[dragon_type][dragon_name][2] = dragon_armor

for current_dragon_type in dragons_dict:
    total_damage = 0
    total_health = 0
    total_armor = 0

    for current_dragon_name in dragons_dict[current_dragon_type]:
        total_damage += dragons_dict[current_dragon_type][current_dragon_name][0]
        total_health += dragons_dict[current_dragon_type][current_dragon_name][1]
        total_armor += dragons_dict[current_dragon_type][current_dragon_name][2]

    average_damage = total_damage/len(dragons_dict[current_dragon_type])
    average_health = total_health/len(dragons_dict[current_dragon_type])
    average_armor = total_armor/len(dragons_dict[current_dragon_type])

    print(f"{current_dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for current_dragon_name in sorted(dragons_dict[current_dragon_type]):
        print(f"-{current_dragon_name} -> damage: {dragons_dict[current_dragon_type][current_dragon_name][0]}\
, health: {dragons_dict[current_dragon_type][current_dragon_name][1]}\
, armor: {dragons_dict[current_dragon_type][current_dragon_name][2]}")

