def odd_even_sum(number_to_sum):
    sum_odd = 0
    sum_even = 0
    for digit in number_to_sum:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    return sum_odd, sum_even

number = input()

odd_digits, even_digits = odd_even_sum(number)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")