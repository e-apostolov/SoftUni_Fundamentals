def fire(some_ship, some_index, some_damage):
    if some_index in range(len(some_ship) - 1):
        some_ship[some_index] -= some_damage
        if some_ship[some_index] <= 0:
            return ("You won! The enemy ship has sunken.")
    return some_ship

def defend(some_ship, first_index, second_index, some_damage):
    checl = len(some_ship)
    if first_index in range(len(some_ship)) and second_index in range(len(some_ship)):
        for index in range(first_index, second_index + 1):
            some_ship[index] -= some_damage
            if some_ship[index] <= 0:
                return ("You lost! The pirate ship has sunken.")
                break
    return some_ship

def repair(some_ship, some_index, some_health):
    if some_index in range(len(some_ship) - 1):
        some_ship[some_index] += some_health
        if some_ship[some_index] > max_health:
            some_ship[some_index] = max_health
    return some_ship


def status(pirate_ship):
    sections_to_repair_pirate = [number for number in pirate_ship if number < 0.2 * max_health]
    print(f"{len(sections_to_repair_pirate)} sections need repair.")

pirate_ship = [int(number) for number in input().split(">")]
war_ship = [int(number) for number in input().split(">")]
max_health = int(input())
battle_ongoing = True

while True:
    command = input()
    if command == "Retire":
        break
    elif command == "Status":
        status(pirate_ship)
        continue
    else:
        command = command.split()
        action = command[0]
        index = int(command[1])

    if action == "Fire":
        damage = int(command[2])
        result = fire(war_ship, index, damage)
        if isinstance(result, str):
            print(result)
            battle_ongoing = False
            break

    elif action == "Defend":
        end_idex = int(command[2])
        damage = int(command[3])
        result = defend(pirate_ship, index, end_idex, damage)
        if isinstance(result, str):
            print(result)
            battle_ongoing = False
            break

    elif action == "Repair":
        health = int(command[2])
        repair(pirate_ship, index, health)

if battle_ongoing:

    print(f"Pirate ship status: {sum(pirate_ship)}\n"
        f"Warship status: {sum(war_ship)}")

