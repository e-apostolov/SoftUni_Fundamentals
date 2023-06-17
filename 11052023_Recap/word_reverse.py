word = input()
print(len(word))
reverse_word = ""

for i in range(len(word) -1, -1, -1):
    reverse_word += word[i]

print(reverse_word)
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])

# word = input()
# print(word[::-1])


