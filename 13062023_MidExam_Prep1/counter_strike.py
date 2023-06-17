input_energy = int(input())
battles_won = 0
is_cycle_completed = True

while True:
    input_distance = input()
    if input_distance == "End of battle":
        break
    input_distance = int(input_distance)
    if input_energy <= 0 or input_distance > input_energy:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {input_energy} energy")
        is_cycle_completed = False
        break
    input_energy -= input_distance
    battles_won += 1
    if battles_won % 3 == 0:
        input_energy += battles_won

if is_cycle_completed:
    print(f"Won battles: {battles_won}. Energy left: {input_energy}")


