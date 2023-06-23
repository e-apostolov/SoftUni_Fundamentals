input_times = input().split()
input_times_int = []
left_side_time = 0
right_side_time = 0
for time in input_times:
    input_times_int.append(int(time))

finish_line = len(input_times_int) // 2
left_side = input_times_int[0:finish_line]
right_side = input_times_int[finish_line + 1:]
right_side.reverse()

for left_times in left_side:
    left_side_time += left_times
    if left_times == 0:
        left_side_time *= 0.8
for right_times in right_side:
    right_side_time += right_times
    if right_times == 0:
        right_side_time *= 0.8

if left_side_time < right_side_time:
    print(f"The winner is left with total time: {left_side_time:.1f}")
elif right_side_time < left_side_time:
    print(f"The winner is right with total time: {right_side_time:.1f}")