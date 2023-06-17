group_size = int(input())
adventure_duration = int(input())
total_coins = 0

for current_day in range(1, adventure_duration + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    total_coins += 50 - (2 * group_size)
    if current_day % 3 == 0:
        total_coins -= 3 * group_size
    if current_day % 5 == 0:
        total_coins += 20 * group_size
        if current_day % 3 == 0:
            total_coins -= 2 * group_size

print(f"{group_size} companions received {int(total_coins / group_size)} coins each.")

