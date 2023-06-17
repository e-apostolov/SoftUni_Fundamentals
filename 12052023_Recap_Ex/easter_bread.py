available_budget = float(input())
price_1kg_flour = float(input())
price_1pkg_eggs = price_1kg_flour * 0.75
price_1l_milk = price_1kg_flour * 1.25
one_loaf_price = price_1pkg_eggs + price_1kg_flour + (0.25 * price_1l_milk)
total_loaves = 0
colored_eggs = 0

while True:
    if available_budget < one_loaf_price:
        break
    available_budget -= one_loaf_price
    total_loaves += 1
    colored_eggs += 3
    if total_loaves % 3 == 0:
        colored_eggs -= ((total_loaves) - 2)

print(f"You made {total_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {available_budget:.2f}BGN left.")






