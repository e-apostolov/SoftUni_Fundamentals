input_data = input().split()

stock = {}

for i in range(0, len(input_data), 2):
    product = input_data[i]
    quantity = int(input_data[i + 1])
    stock[product] = quantity

print(stock)
    