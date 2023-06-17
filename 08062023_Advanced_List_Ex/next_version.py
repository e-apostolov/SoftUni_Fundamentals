input_version = [int(n) for n in input().split(".")]
input_version[-1] += 1

for index in range(len(input_version) -1, -1, -1):
     if input_version[index] > 9:
         input_version[index] = 0
         if index - 1 >= 0:
            input_version[index - 1] += 1

print(".".join(map(str, input_version)))
