number_of_entries = int(input())
open_brackets = 0
closing_brackets = 0
double_brackets = False

for entry in range(number_of_entries):
    current_entry = input()
    if current_entry == "(":
        if double_brackets:
            break
        open_brackets += 1
        double_brackets = True
    elif current_entry == ")":
        closing_brackets += 1
        double_brackets = False
if open_brackets != closing_brackets or double_brackets:
    print("UNBALANCED")
else:
    print("BALANCED")