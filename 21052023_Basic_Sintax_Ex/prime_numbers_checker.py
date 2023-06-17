input_number = int(input())
number_of_dividers = 0

for divider in range(1, input_number + 1):
    if input_number % divider == 0:
        number_of_dividers += 1

if number_of_dividers > 2:
    print(False)
else:
    print(True)




