def cabin_distribution(passengers, cabins):
    for cabin in range(len(cabins)):
        available_seats = 4 - cabins[cabin]
        if available_seats > 0 and passengers >= available_seats:
            cabins[cabin] += available_seats
            passengers -= available_seats
        elif available_seats > 0 and passengers < available_seats:
            cabins[cabin] += passengers
            passengers = 0

    if passengers <= 0 and min(cabins) < 4:
        result = f"The lift has empty spots!\n" \
                 f"{' '.join(map(str, cabins))}"
    elif passengers > 0 and min(cabins) == 4:
        result = f"There isn't enough space! {passengers} people in a queue!\n" \
                 f"{' '.join(map(str, cabins))}"
    elif passengers == 0 and min(cabins) == 4:
        result = ' '.join(map(str, cabins))

    return result


number_of_passengers = int(input())
cabins = [int(number) for number in input().split()]

print(cabin_distribution(number_of_passengers, cabins))

