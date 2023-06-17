char_index_start = int(input())
char_index_end = int(input())

for character in range(char_index_start, char_index_end + 1):
    print(f"{chr(character)}", end=" ")