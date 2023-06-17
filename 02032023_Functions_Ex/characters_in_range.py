def character_collection(first, second):
    characters = []
    for current_element in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_element))
    return (" ".join(characters))


first_character = input()
second_character = input()
print(character_collection(first_character, second_character))
