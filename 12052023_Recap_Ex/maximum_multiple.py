# divisor = int(input())
# boundary = int(input())
# max_number = 0
#
# for n in range(0, boundary +1):
#     if n % divisor == 0:
#         max_number = n
#
# print(max_number)

divisor = int(input())
boundary = int(input())

for n in range(boundary, divisor -1, -1):
    if n % divisor == 0:
        print(n)
        break