words = input().split(' ')
given_palindrome = input()
list_palindrome = []
counter = 0
starting_index = 0
for iteration in range(len(words)):

    current_word = words[starting_index]
    palindrome = current_word[::-1]
    if current_word == palindrome:
        list_palindrome.append(palindrome)

    if given_palindrome == current_word:
        counter += 1
    starting_index += 1

print(list_palindrome)
print(f"Found palindrome {counter} times")
