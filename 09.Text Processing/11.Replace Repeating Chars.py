text = input()
new_text = ''
unique_counter = 0

for index in range(len(text) - 1):
    if text[index] != text[index + 1] and unique_counter == 0:
        new_text += text[index]

    if text[index] == text[index + 1]:
        if unique_counter == 0:
            new_text += text[index]
            unique_counter += 1
    else:
        unique_counter = 0
        
if text[-1] != text[-2]:
    new_text += text[-1]
    print(new_text)
else:
    print(new_text)
