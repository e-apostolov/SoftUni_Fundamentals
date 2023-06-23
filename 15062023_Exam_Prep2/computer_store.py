
order_input = input()
total_cost = 0

while order_input != "special" and order_input != "regular":
    order_input = float(order_input)
    if order_input < 0:
        print("Invalid price!")
    else:
        total_cost += order_input
    order_input = input()

if total_cost == 0:
    print("Invalid order!")
else:
    taxes = total_cost * 0.2
    total_cost_incl_taxes = total_cost + taxes
    if order_input == "special":
        total_cost_incl_taxes = total_cost_incl_taxes * 0.9
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_cost:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_cost_incl_taxes:.2f}$\n")







