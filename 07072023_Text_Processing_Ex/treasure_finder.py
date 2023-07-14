input_key = input().split()

while True:
    command = input()
    input_key_index = 0
    if command == "find":
        break
    decrypted_message = ""

    for character in command:
        if input_key_index == len(input_key):
            input_key_index = 0
        decrypted_message += chr(ord(character) - int(input_key[input_key_index]))
        input_key_index += 1

    coordinate_start_index = decrypted_message.index("<")
    coordinate_end_index = decrypted_message.index(">")
    treasure_coordinates = decrypted_message[coordinate_start_index + 1: coordinate_end_index]

    decrypted_message = decrypted_message.split("&")
    type_treasure = decrypted_message[1]

    print(f"Found {type_treasure} at {treasure_coordinates}")
