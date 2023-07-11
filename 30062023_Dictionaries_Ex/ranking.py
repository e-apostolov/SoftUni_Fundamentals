contests_dict = {}
users_results = {}
top_user = ""
top_score = 0

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password_of_contest = command.split(":")
    contests_dict[contest] = password_of_contest

while True:
    command = input()
    if command == "end of submissions":
        break
    sub_contest, sub_password, sub_username, sub_points = command.split("=>")
    sub_points = int(sub_points)
    if sub_contest in contests_dict and sub_password == contests_dict[sub_contest]:
        if sub_username not in users_results:
            users_results[sub_username] = {sub_contest: sub_points}
        elif sub_contest in users_results[sub_username]:
            if sub_points > users_results[sub_username][sub_contest]:
                users_results[sub_username][sub_contest] = sub_points
        elif sub_contest not in users_results[sub_username]:
            users_results[sub_username][sub_contest] = sub_points


for user in users_results:
    current_user_top_score = 0
    for contest in users_results[user]:
        current_user_top_score += users_results[user][contest]
    if current_user_top_score > top_score:
        top_score = current_user_top_score
        top_user = user


print(f"Best candidate is {top_user} with total {top_score} points.\nRanking:")
for key, value in sorted(users_results.items()):
    print(key)
    for contest, results in sorted(users_results[key].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {results}")




