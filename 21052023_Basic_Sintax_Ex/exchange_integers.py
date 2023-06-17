# first_number = int(input())
# second_number = int(input())
#
# print("Before:")
# print(f"a = {first_number}")
# print(f"b = {second_number}")
# print("After:")
# print(f"a = {second_number}")
# print(f"b = {first_number}")

a = int(input())
b = int(input())

print(f"Before: \n"
      f"a = {a} \n"
      f"b = {b}")
temp_a = a
a = b
b = temp_a

print(f"After: \n"
      f"a = {a} \n"
      f"b = {b}")
