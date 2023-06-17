def check_rooms(num_rooms):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1, num_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
            total_needed_chairs += abs(difference)
        else:
            total_free_chairs += difference

    return total_free_chairs, total_needed_chairs

number_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_rooms(number_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")