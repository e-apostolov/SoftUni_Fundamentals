def solve(number):
    mask = 1 << 1
    least_significant_number = number & mask
    return least_significant_number >> 1


input_number = int(input())

print(solve(input_number))
