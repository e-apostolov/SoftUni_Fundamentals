# number_of_entries = int(input())
# key_word = input()
# sentence = []
# filtered_sentence = []
#
# for entries in range(number_of_entries):
#     current_entry = input()
#     sentence.append(current_entry)
#
# print(sentence)
#
# for entries in range(len(sentence)):
#     if key_word in sentence[entries]:
#         filtered_sentence.append(sentence[entries])
#
# print(filtered_sentence)
#

number_of_entries = int(input())
key_word = input()
sentence = []
filtered_sentence = []

for entries in range(number_of_entries):
    current_entry = input()
    sentence.append(current_entry)

print(sentence)

for entries in sentence:
    if key_word in entries:
        filtered_sentence.append(entries)

print(filtered_sentence)



