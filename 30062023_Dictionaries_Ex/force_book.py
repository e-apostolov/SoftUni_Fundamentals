forces_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        check = False
        for key, values in forces_dict.items():
            if force_user in values:
                check = True
                break
        if check is False:
            if force_side not in forces_dict.keys():
                forces_dict[force_side] = []
            forces_dict[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        if force_side not in forces_dict.keys():
            forces_dict[force_side] = []
        for key, values in forces_dict.items():
            if force_user in values:
                values.remove(force_user)
        forces_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in forces_dict.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for index in range(len(users)):
            print(f"! {users[index]}")

