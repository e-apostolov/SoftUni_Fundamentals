def decipher_string(some_word):
    number_index = len(list(filter(lambda x: x.isnumeric(), some_word)))
    first_word = some_word[:number_index]
    first_word = chr(int(first_word))
    second_word = [*some_word[number_index:]]
    second_word[0], second_word[-1] = second_word[-1], second_word[0]
    second_word = ''.join(second_word)
    return first_word + second_word

input_string = input().split()
new_string = " ".join(decipher_string(word) for word in input_string)
print(new_string)