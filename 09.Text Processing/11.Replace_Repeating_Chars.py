given_text = input()
replaced_text = ''
last_letter = ''

for index in range(len(given_text) - 1):
    if given_text[index] != given_text[index + 1]:
        replaced_text += given_text[index]
        last_letter = given_text[index]
if given_text[-1] != last_letter:
    replaced_text += given_text[-1]
    print(replaced_text)
else:
    print(replaced_text)