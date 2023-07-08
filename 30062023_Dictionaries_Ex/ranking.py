contests_dict = {}
submissions_dict = {}

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
    submissions_dict[sub_contest] = {"sub_password": "", sub_username: "", sub_points: ""]
    submissions_dict[sub_contest][sub_password] = sub_password
    submissions_dict[sub_contest][sub_username] = sub_username
    submissions_dict[sub_contest][sub_points] = sub_points

if submissions_dict[sub_contest] in contests_dict[contest] and submissions_dict[sub_contest][sub_password] == contests_dict[contest]:
    




