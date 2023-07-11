users_points_dict = {}
contests_dict = {}
points_dict = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)
    if username not in users_points_dict:
        users_points_dict[username] = {contest: points}
    elif username in users_points_dict:
        if contest in users_points_dict[username]:
            if points > users_points_dict[username][contest]:
                users_points_dict[username][contest] = points
        else:
            users_points_dict[username].update({contest: points})

    if contest not in contests_dict:
        contests_dict[contest] = {username: points}
    elif contest in contests_dict:
        if username in contests_dict[contest]:
            if points > contests_dict[contest][username]:
                contests_dict[contest][username] = points
        else:
            contests_dict[contest].update({username: points})

for contest in contests_dict:
    print(f"{contest}: {len(contests_dict[contest])} participants")
    i = 1
    for participants, points in sorted(contests_dict[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f"{i}. {participants} <::> {points}")
        i += 1

print("Individual standings:")

for user in users_points_dict:
    current_user_points = 0
    for contest in users_points_dict[user]:
        current_user_points += users_points_dict[user][contest]
    points_dict[user] = current_user_points

i = 1
for sorted_user, sorted_points in sorted(points_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{i}. {sorted_user} -> {sorted_points}")
    i += 1








