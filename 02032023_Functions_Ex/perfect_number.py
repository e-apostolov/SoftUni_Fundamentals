def perfect_number(some_number:int) -> str:
    divisor_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisor_sum += divisor
    if some_number == divisor_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

input_number = int(input())

print(perfect_number(input_number))
