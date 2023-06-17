input_string = input()
input_string = input_string.lower()
search_items_list = ["sand", "water", "fish", "sun"]
counter = 0

for search_item in search_items_list:
    if search_item in input_string:
        counter += input_string.count(search_item)

print(counter)