number_of_lines = int(input())
parking_lot = {}

for i in range(number_of_lines):
    command = input().split()
    action, username = command[0], command[1]
    if action == "register":
        license_plate = command[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
    elif action == "unregister":
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

for users, plates in parking_lot.items():
    print(f"{users} => {plates}")
