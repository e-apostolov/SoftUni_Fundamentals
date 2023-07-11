dwarfs_dict = {}
colors_dict = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    dwarf_id = dwarf_name + ":" + dwarf_hat_color
    if dwarf_id not in dwarfs_dict:
        dwarfs_dict[dwarf_id] = [dwarf_hat_color, dwarf_physics]

    elif dwarf_id in dwarfs_dict:
        if dwarf_hat_color not in dwarfs_dict[dwarf_id]:
            dwarfs_dict[dwarf_id] = [dwarf_hat_color, dwarf_physics]
        elif dwarf_hat_color in dwarfs_dict[dwarf_id]:
            if dwarf_physics > dwarfs_dict[dwarf_id][1]:
                dwarfs_dict[dwarf_id][1] = dwarf_physics


for dwarf in dwarfs_dict:
    if dwarfs_dict[dwarf][0] not in colors_dict:
        colors_dict[dwarfs_dict[dwarf][0]] = 1
    elif dwarfs_dict[dwarf][0] in colors_dict:
        colors_dict[dwarfs_dict[dwarf][0]] += 1


sorted_dwarfs = dict(sorted(dwarfs_dict.items(), key=lambda x: (x[1][1], colors_dict[x[1][0]]), reverse=True))
for key, value in sorted_dwarfs.items():
    name = key.split(":")
    print(f"({name[1]}) {name[0]} <-> {value[1]}")

