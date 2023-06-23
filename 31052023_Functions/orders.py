def price_calculator(some_product=str, some_quantity=int):
    total_price = 0
    if some_product == "coffee":
        total_price = some_quantity * 1.50
    elif some_product == "water":
        total_price = some_quantity
    elif some_product == "coke":
        total_price = some_quantity * 1.40
    else:
        total_price = some_quantity * 2
    return total_price

type_of_product = input()
quantity_of_product = int(input())

print(f"{price_calculator(type_of_product, quantity_of_product):.2f}")