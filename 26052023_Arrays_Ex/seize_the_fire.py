fire_details_input = input().split("#")
amount_of_water = int(input())
effort = 0
fires = []

for fire in fire_details_input:
    type_of_fire, value_of_fire = fire.split(" = ")
    value_of_fire = int(value_of_fire)
    is_fire_value_valid = False
    if type_of_fire == "High" and 81 <= value_of_fire <= 125:
        is_fire_value_valid = True
    elif type_of_fire == "Medium" and 51 <= value_of_fire <= 80:
        is_fire_value_valid = True
    elif type_of_fire == "Low" and 1 <= value_of_fire <= 50:
        is_fire_value_valid = True
    if is_fire_value_valid:
        if amount_of_water >= value_of_fire:
            amount_of_water -= value_of_fire
            effort += value_of_fire * 0.25
            fires.append(value_of_fire)

print("Cells:")
for fire in fires:
    print(f" - {fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(fires)}")

