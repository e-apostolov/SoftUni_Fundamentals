duration_days = int(input())
plunder_per_day = int(input())
plunder_target = float(input())
total_plunder = 0

for day_index in range(1, duration_days + 1):
    current_plunder = plunder_per_day
    if day_index % 3 == 0:
        current_plunder += 0.5 * current_plunder
    total_plunder += current_plunder
    if day_index % 5 == 0:
        total_plunder *= 0.70

if total_plunder >= plunder_target:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")

else:
    print(f"Collected only {total_plunder/plunder_target * 100:.2f}% of the plunder.")
