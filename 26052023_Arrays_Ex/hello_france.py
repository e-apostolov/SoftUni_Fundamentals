items_collection_input = input().split("|")
total_budget = int(input())
profit = 0
revenue = 0
sell_prices=[]

for item in items_collection_input:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    is_price_valid = False
    if item_type == "Clothes":
        if item_price <= 50.00:
            is_price_valid = True
    elif item_type == "Shoes":
        if item_price <= 35.00:
            is_price_valid = True
    elif item_type == "Accessories":
        if item_price <= 20.50:
            is_price_valid = True
    if is_price_valid:
        if total_budget >= item_price:
            total_budget -= item_price
            new_price = item_price * 1.40
            revenue += new_price
            profit += new_price - item_price
            sell_prices.append(new_price)
            # print(f"{new_price:.2f}", end=" ") #option 1

for sell_price in sell_prices:                   #option 2
    print(f"{sell_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total_budget + revenue >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")



