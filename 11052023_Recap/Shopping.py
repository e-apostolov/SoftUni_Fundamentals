budget = int(input())
total_price = 0

while True:
    price = input()

    if price == "End":
        print("You bought everything needed.")
        break

    price = int(price)

    if total_price + price > budget:
        print("You went in overdraft!")
        break

    total_price += price
