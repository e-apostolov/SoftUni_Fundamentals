def merge_word(some_string, start_index, end_index):
    if int(start_index) < 0:
        start_index = 0
    if int(end_index) > len(some_string) - 1:
        end_index = len(some_string) - 1
    working_string = some_string[int(start_index):int(end_index) + 1]
    message_to_add = "".join(working_string)
    # new_string = []
    diff_indices = int(end_index) - int(start_index)
    if end_index == len(some_string):
        diff_indices -= 1

    for i in range(diff_indices + 1):
        if len(some_string) > 0:
            some_string.pop(int(start_index))
        else:
            continue
    some_string.insert(int(start_index), message_to_add)
    # for index in range(len(some_string)):
    #     if index < int(start_index) or index > int(end_index):
    #         if some_string[index] != " " or some_string != "":
    #             new_string.append(some_string[index])
    # new_string.insert(int(start_index), working_string)
    return some_string


def divide_word(some_string, some_index, partitions):
    word_to_be_divided = some_string.pop(int(some_index))
    letters_in_each_new_string = len(word_to_be_divided) // int(partitions)
    if letters_in_each_new_string < 1:
        letters_in_each_new_string = 1
    start = 0
    for additions in range(int(partitions)):
        if additions == int(partitions) - 1:
            some_string.insert(some_index, word_to_be_divided[start:])
            break
        else:
            some_string.insert(int(some_index), word_to_be_divided[start:start + int(letters_in_each_new_string)])
        start += letters_in_each_new_string
        some_index = int(some_index) + 1
    return some_string

input_string = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    action, start_index, end_index_or_partitions = command.split()
    if action == "merge":
        output_string = merge_word(input_string, start_index, end_index_or_partitions)
    elif action == "divide":
        output_string = divide_word(input_string, start_index, end_index_or_partitions)
    input_string = output_string

print(" ".join(output_string))