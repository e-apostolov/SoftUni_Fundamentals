import re
input_string = input()

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2,2}/\d{2,2}/\d{2,2})\1(\d{1,5})\1"
matches = re.finditer(pattern, input_string)
total_calories = 0
food_items = []

for match in matches:
    item = match.group(2)
    date = match.group(3)
    calories = int(match.group(4))
    total_calories += calories
    food_items.append([item, date, calories])

available_food = total_calories // 2000

print(f"You have food to last you for: {available_food} days!")
for food_item in food_items:
    print(f"Item: {food_item[0]}, Best before: {food_item[1]}, Nutrition: {food_item[2]}")

