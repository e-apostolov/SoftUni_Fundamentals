products = {}
command = input().split()

while command[0] != "buy":
    product, price, quantity = command[0], float(command[1]), int(command[2])

    if product not in products.keys():
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity

    command = input().split()

for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")