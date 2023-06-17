def top_5_numbers(some_numbers):
    average_number = sum(some_numbers)/len(some_numbers)
    top_5_list = [number for number in some_numbers if number > average_number]
    top_5_list.sort(reverse=True)
    if len(top_5_list) > 5:
        top_5_list = top_5_list[:5]
    if len(top_5_list) < 1:
        result = "No"
    else:
        result = " ".join(map(str, top_5_list))
    return result

input_numbers = [int(number) for number in input().split()]
print(top_5_numbers(input_numbers))