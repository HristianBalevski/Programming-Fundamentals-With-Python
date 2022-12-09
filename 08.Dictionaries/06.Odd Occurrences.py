data = [str(w).lower() for w in input().split()]
words_to_print = []

for word in data:
    count = int(data.count(word))

    if count % 2 !=0:
        if word not in words_to_print:
            words_to_print.append(word)
print(" ".join(words_to_print))
