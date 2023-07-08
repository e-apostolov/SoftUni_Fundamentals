from math import ceil

number = int(input())
digit = int(input())
counter = 0

while number > 0:
    remainder = 0
    remainder = number % 2
    if remainder == digit:
        counter += 1
    number -= ceil(number / 2)


print(counter)
