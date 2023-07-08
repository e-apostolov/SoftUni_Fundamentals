input_stock = input().split()

stock = {}

for i in range(0, len(input_stock), 2):
    product = input_stock[i]
    quantity = int(input_stock[i + 1])
    stock[product] = quantity

products_to_search = input().split()

for product in products_to_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")