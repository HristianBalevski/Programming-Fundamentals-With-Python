txt = input()
already_counted = []

for char in txt:
    if char in already_counted or char == ' ':
        continue
    result = txt.count(char)
    already_counted.append(char)
    print(f'{char} -> {result}')
