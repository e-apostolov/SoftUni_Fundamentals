players_dict = {}
players_total_points = {}

while True:
    command = input()
    if command == "Season end":
        break

    elif " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_dict:
            players_dict[player] = {position: skill}
        elif player in players_dict:
            if position not in players_dict[player]:
                players_dict[player].update({position: skill})
            elif position in players_dict[player]:
                if players_dict[player][position] < skill:
                    players_dict[player][position] = skill

    elif " vs " in command:
        player_1, player_2 = command.split(" vs ")
        if player_1 in players_dict and player_2 in players_dict:
            player_1_total_points = 0
            player_2_total_points = 0
            for player in players_dict:
                for positions in players_dict[player]:
                    if player == player_1:
                        player_1_total_points += players_dict[player_1][positions]
                    elif player == player_2:
                        player_2_total_points += players_dict[player_2][positions]

            for pos1 in players_dict[player_1]:
                for pos2 in players_dict[player_2]:
                    if pos2 == pos1:
                        if player_1_total_points > player_2_total_points:
                            del players_dict[player_2]
                            break
                        elif player_2_total_points > player_1_total_points:
                            del players_dict[player_1]
                            break
                break

for players in players_dict:
    for positions, points in players_dict[players].items():
        if players not in players_total_points:
            players_total_points[players] = points
        else:
            players_total_points[players] += points

for players, points in sorted(players_total_points.items(), key=lambda x: (-x[1], x[0])):
    if points != 0:
        print(f"{players}: {points} skill")

        for positions, skills in sorted(players_dict[players].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {positions} <::> {skills}")


