rooms_sequence = [room for room in input().split("|")]
health = 100
bitcoins = 0
best_room = 0
is_dead = False

for room_index in range(len(rooms_sequence)):
    best_room = room_index + 1
    action, amount = rooms_sequence[room_index].split()
    amount = int(amount)
    if action == "potion":
        if health + amount >= 100:
            amount -= (health + amount - 100)
            health = 100
        else:
            health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health <= 0:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_room}")
            is_dead = True
            break
        else:
            print(f"You slayed {action}.")


if not is_dead:
    print(f"You've made it!\n"
        f"Bitcoins: {bitcoins}\n"
        f"Health: {health}")