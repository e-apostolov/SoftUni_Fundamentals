input_targets = [int(number) for number in input().split()]

input_shot = input()
shot_list = input_targets

while input_shot != "End":
    input_shot = int(input_shot)
    if input_shot in range(len(input_targets)):
        target_value = input_targets[input_shot]
        input_targets[input_shot] = -1
        for target in range(len(input_targets)):
            if input_targets[target] != -1:
                if input_targets[target] > target_value:
                    input_targets[target] -= target_value
                elif input_targets[target] <= target_value:
                    input_targets[target] += target_value
    input_shot = input()

count_shot_targets = input_targets.count(-1)
input_targets = " ".join(map(str, input_targets))


print(f"Shot targets: {count_shot_targets} -> {input_targets}")



