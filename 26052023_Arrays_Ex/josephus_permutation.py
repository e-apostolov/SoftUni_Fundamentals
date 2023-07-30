
input_list = [x for x in input().split()]
input_number = int(input())
eliminated_list = []
current_index = 0

while input_list:
    current_index += input_number - 1
    if current_index >= len(input_list):
        while current_index >= len(input_list):
            current_index -= len(input_list)

    eliminated_list.append(input_list[current_index])
    input_list.pop(current_index)

print(f"[{','.join(eliminated_list)}]")