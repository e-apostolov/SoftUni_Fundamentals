def cast_spell(heroes_dict, current_command):
    current_hero_name = current_command[1]
    mana_points_needed = int(current_command[2])
    spell_name = current_command[3]
    if heroes_dict[current_hero_name]["MANA"] >= mana_points_needed:
        heroes_dict[current_hero_name]["MANA"] -= mana_points_needed
        print(f"{current_hero_name} has successfully cast {spell_name} "
              f"and now has {heroes_dict[current_hero_name]['MANA']} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")
    return heroes_dict


def take_damage(heroes_dict, current_command):
    current_hero_name = current_command[1]
    damage = int(current_command[2])
    attacker = current_command[3]
    heroes_dict[current_hero_name]["HP"] -= damage
    if heroes_dict[current_hero_name]["HP"] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and "
              f"now has {heroes_dict[current_hero_name]['HP']} HP left!")
    else:
        print(f"{current_hero_name} has been killed by {attacker}!")
        del heroes_dict[current_hero_name]
    return heroes_dict


def recharge(heroes_dict, current_command):
    current_hero_name = current_command[1]
    amount = int(current_command[2])
    recovered = amount
    heroes_dict[current_hero_name]['MANA'] += amount
    if heroes_dict[current_hero_name]['MANA'] > 200:
        recovered = amount - (heroes_dict[current_hero_name]["MANA"] - 200)
        heroes_dict[current_hero_name]["MANA"] = 200
    print(f"{current_hero_name} recharged for {recovered} MP!")
    return heroes_dict


def heal(heroes_dict, current_command):
    current_hero_name = current_command[1]
    amount = int(current_command[2])
    recovered = amount
    heroes_dict[current_hero_name]['HP'] += amount
    if heroes_dict[current_hero_name]['HP'] > 100:
        recovered = amount - (heroes_dict[current_hero_name]["HP"] - 100)
        heroes_dict[current_hero_name]["HP"] = 100
    print(f"{current_hero_name} healed for {recovered} HP!")
    return heroes_dict


heroes = {}

number_of_heroes = int(input())

for hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"HP": int(hit_points), "MANA": int(mana_points)}

while True:
    command = input()
    if command == "End":
        break
    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        heroes = cast_spell(heroes, command)
    elif action == "TakeDamage":
        heroes = take_damage(heroes, command)
    elif action == "Recharge":
        heroes = recharge(heroes, command)
    elif action == "Heal":
        heroes = heal(heroes, command)

for hero_name, values in heroes.items():
    print(hero_name)
    print(f"  HP: {values['HP']}")
    print(f"  MP: {values['MANA']}")
