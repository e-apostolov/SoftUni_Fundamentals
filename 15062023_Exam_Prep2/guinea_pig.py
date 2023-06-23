
input_food = float(input())
input_hay = float(input())
input_cover = float(input())
guinea_weight = float(input())

input_food = input_food * 1000
input_hay = input_hay * 1000
input_cover = input_cover * 1000
guinea_weight = guinea_weight * 1000

for days in range(1, 31):
    input_food -= 300
    if days % 2 == 0:
        input_hay -= input_food * 0.05
    if days % 3 == 0:
        input_cover -= guinea_weight / 3

if input_food <= 0 or input_hay <= 0 or input_cover <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {input_food/1000:.2f}, Hay: {input_hay/1000:.2f}, Cover: {input_cover/1000:.2f}.")