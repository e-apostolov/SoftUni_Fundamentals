words = input().split()
search_palindrome = input()
palindrome_list = []
for word in words:
    if word == word[::-1]:
        palindrome_list.append(word)

palindrome_count = palindrome_list.count(search_palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")
