import re


def valid_destination(destination_data):
    pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
    travel_points = 0
    valid_destinations = []
    result = re.finditer(pattern, destination_data)

    for current_destination in result:
        valid_destinations.append(current_destination.group(2))
        travel_points += len(current_destination.group(2))

    return f"Destinations: {', '.join(valid_destinations)}\nTravel Points: {travel_points}"


input_string = input()
print(valid_destination(input_string))
