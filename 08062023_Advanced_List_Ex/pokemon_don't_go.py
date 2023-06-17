# input_sequence = [int(number) for number in input().split()]
# sum_removed_elements = 0
#
# while input_sequence:
#     input_index = int(input())
#     deleted_num = 0
#     if 0 <= input_index < len(input_sequence):
#         deleted_num = input_sequence.pop(input_index)
#     elif input_index < 0:
#         deleted_num = input_sequence[0]
#         input_sequence[0] = input_sequence[-1]
#     elif input_index > len(input_sequence) - 1:
#         deleted_num = input_sequence[-1]
#         input_sequence[-1] = input_sequence[0]
#     sum_removed_elements += deleted_num
#     for element in range(len(input_sequence)):
#         if input_sequence[element] <= deleted_num:
#             input_sequence[element] += deleted_num
#         elif input_sequence[element] > deleted_num:
#             input_sequence[element] -= deleted_num
# print(sum_removed_elements)

# input_sequence = [int(number) for number in input().split()]
# removed_elements = 0
#
# while input_sequence:
#     input_index = int(input())
#     value_of_index = 0
#     if 0 <= input_index < len(input_sequence):
#         value_on_index = input_sequence.pop(input_index)
#     elif input_index < 0:
#         value_on_index = input_sequence[0]
#         input_sequence[0] = input_sequence[-1]
#     elif input_index > len(input_sequence) - 1:
#         value_on_index = input_sequence[-1]
#         input_sequence[-1] = input_sequence[0]
#     removed_elements += value_on_index
#     for element in range(len(input_sequence)):
#         if input_sequence[element] <= value_on_index:
#             input_sequence[element] += value_on_index
#         elif input_sequence[element] > value_on_index:
#             input_sequence[element] -= value_on_index
#
#
# print(removed_elements)

input_sequence = [int(number) for number in input().split()]
removed_elements = []

while input_sequence:
    input_index = int(input())
    if 0 <= input_index < len(input_sequence):
        value_on_index = input_sequence[input_index]
        input_sequence.pop(input_index)
    elif input_index < 0:
        value_on_index = input_sequence[0]
        input_sequence[0] = input_sequence[-1]
    elif input_index > len(input_sequence) - 1:
        value_on_index = input_sequence[-1]
        input_sequence[-1] = input_sequence[0]
    removed_elements.append(value_on_index)
    for element in range(len(input_sequence)):
        if input_sequence[element] <= value_on_index:
            input_sequence[element] += value_on_index
        elif input_sequence[element] > value_on_index:
            input_sequence[element] -= value_on_index
result = sum(removed_elements)
print(result)
