def plunder(cities, current_command):
    current_town, current_people, current_gold = current_command[1], current_command[2], current_command[3]
    current_people, current_gold = int(current_people), int(current_gold)
    cities[current_town][0] -= current_people
    cities[current_town][1] -= current_gold

    print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")

    if cities[current_town][0] <= 0 or cities[current_town][1] <= 0:
        print(f"{current_town} has been wiped off the map!")
        del cities[current_town]

    return cities


def prosper(cities, current_command):
    current_town, current_gold = current_command[1], current_command[2]
    current_gold = int(current_gold)
    if current_gold < 0:
        print("Gold added cannot be a negative number!")
        return cities
    cities[current_town][1] += current_gold
    print(f"{current_gold} gold added to the city treasury. {current_town} now has {cities[current_town][1]} gold.")
    return cities


cities_dict = {}

while True:
    command = input()
    if command == "Sail":
        break

    command = command.split("||")
    city, population, gold = command[0], command[1], command[2]
    population, gold = int(population), int(gold)

    if city not in cities_dict:
        cities_dict[city] = [population, gold]

    else:
        cities_dict[city][0] += population
        cities_dict[city][1] += gold


while True:
    command = input()
    if command == "End":
        break

    command = command.split("=>")
    action = command[0]

    if action == "Plunder":
        cities_dict = plunder(cities_dict, command)
    elif action == "Prosper":
        cities_dict = prosper(cities_dict, command)


if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for key, value in cities_dict.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")