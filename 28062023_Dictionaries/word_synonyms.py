count_of_words = int(input())
synonyms_dict = {}

for index in range(count_of_words):
    word = input()
    synonym = input()
    if word not in synonyms_dict.keys():
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for word, synonym in synonyms_dict.items():
    print(f"{word} - {', '.join(synonym)}")
