gift_list = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command_split = command.split()
    command_type = command_split[0]
    command_gift = command_split[1]
    if len(command_split) > 2:
        command_index = int(command_split[2])
    if command_type == "OutOfStock":
        for gift_index in range(len(gift_list)):
            if gift_list[gift_index] == command_gift:
                gift_list[gift_index] = "None"
    elif command_type == "Required":
        if 0 <= command_index < len(gift_list):
            gift_list[command_index] = command_gift
    elif command_type == "JustInCase":
        gift_list[-1] = command_gift

while "None" in gift_list:
    gift_list.remove("None")
print(*gift_list, sep=" ")

