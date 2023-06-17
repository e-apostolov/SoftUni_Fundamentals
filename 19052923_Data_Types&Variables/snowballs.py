number_of_snowballs_made = int(input())
highest_value = 0
winner_weight = 0
winner_time_to_target = 0
winner_quality = 0

for snowball in range(number_of_snowballs_made):
    snowball_weight = int(input())
    snowball_time_to_target = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time_to_target) ** snowball_quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        winner_weight = snowball_weight
        winner_time_to_target = snowball_time_to_target
        winner_quality = snowball_quality

print(f"{winner_weight} : {winner_time_to_target} = {int(highest_value)} ({winner_quality})")


