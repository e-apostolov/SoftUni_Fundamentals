def drive(current_cars, current_command):
    current_car, current_distance, current_fuel = current_command[1], current_command[2], current_command[3]
    current_distance, current_fuel = int(current_distance), int(current_fuel)

    if current_fuel > current_cars[current_car][1]:
        print("Not enough fuel to make that ride")

    else:
        current_cars[current_car][1] -= current_fuel
        print(f"{current_car} driven for {current_distance} kilometers. {current_fuel} liters of fuel consumed.")
        current_cars[current_car][0] += current_distance
        if current_cars[current_car][0] >= 100000:
            del current_cars[current_car]
            print(f"Time to sell the {current_car}!")


def refuel(current_cars, current_command):
    current_car, current_fuel = current_command[1], current_command[2]
    current_fuel = int(current_fuel)

    current_cars[current_car][1] += current_fuel
    refueled_amount = current_fuel
    if current_cars[current_car][1] > 75:
        refueled_amount = current_fuel + (75 - current_cars[current_car][1])
        current_cars[current_car][1] = 75

    print(f"{current_car} refueled with {refueled_amount} liters")


def revert(current_cars, current_command):
    current_car, current_km = current_command[1], current_command[2]
    current_km = int(current_km)
    current_cars[current_car][0] -= current_km
    amount_reverted = current_km

    if current_cars[current_car][0] < 10000:
        current_cars[current_car][0] = 10000
        amount_reverted = amount_reverted + current_km - 10000
    else:
        print(f"{current_car} mileage decreased by {amount_reverted} kilometers")


number_of_cars = int(input())
car_dict = {}

for cars in range(number_of_cars):
    car, milage, fuel = input().split("|")
    car_dict[car] = [int(milage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        drive(car_dict, command)
    elif action == "Refuel":
        refuel(car_dict, command)
    elif action == "Revert":
        revert(car_dict, command)

for key, value in car_dict.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")





