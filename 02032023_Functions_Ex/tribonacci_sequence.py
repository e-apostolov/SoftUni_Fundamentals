def tribonacci(some_number):
    sequence = [1]
    for number in range(1, some_number):
        if len(sequence) < 3:
            sequence.append(number)
        else:
            sequence.append(sum(sequence[-3:]))
    sequence = " ".join(map(str, sequence))
    return sequence


input_number = int(input())
print(tribonacci(input_number))