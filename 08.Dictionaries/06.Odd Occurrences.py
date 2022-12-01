words = input().split()
words_lower = []
already_printed = []

for element in words:
    words_lower.append(element.lower())

for index in range(len(words_lower)):
    searched_word = words_lower[index]
    
    if words_lower.count(searched_word) % 2 != 0:
        if searched_word not in already_printed:
            print(searched_word, end=" ")
            already_printed.append(searched_word)
