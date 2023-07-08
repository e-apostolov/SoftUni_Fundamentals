def solve(number, position):
    mask = ~(1 << position)
    least_significant_number = number & mask
    return least_significant_number


input_number = int(input())
input_position = int(input())

print(solve(input_number, input_position))
