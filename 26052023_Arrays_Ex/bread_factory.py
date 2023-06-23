input_string = input().split("|")
total_energy = 100
total_coins = 100
is_factory_open = True

for day in range(len(input_string)):
    event = input_string[day].split("-")
    event_type = event[0]
    event_value = int(event[1])
    if event_type == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        print(f"You gained {total_energy - current_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            is_factory_open = False
            break

if is_factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

else:
    print(f"Closed! Cannot afford {event_type}.")