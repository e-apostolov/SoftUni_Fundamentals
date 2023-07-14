start_character = ord(input())
end_character = ord(input())
input_string = input()
sum_ord = 0


for character in input_string:
    if start_character < ord(character) < end_character:
        sum_ord += ord(character)

print(sum_ord)