input_number = int(input())
for letter_1 in range(0, input_number):
    for letter_2 in range(0, input_number):
        for letter_3 in range(0, input_number):
            print(f"{chr(97+letter_1)}"
                  f"{chr(97+letter_2)}"
                  f"{chr(97+letter_3)}")

