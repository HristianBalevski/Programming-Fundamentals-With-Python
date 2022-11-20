import re

pattern = r'(?P<Surr>:\:|\*\*)(?P<Emojy>[A-Z][a-z]{2,})(\1)'
text = input()
threshold = 1
emojy_power = 0
emojy_to_print = []

for symbol in text:
    if symbol.isdigit():
        threshold *= int(symbol)
print(f'Cool threshold: {threshold}')
valid_emojy = re.finditer(pattern, text)
emo_counter = 0
for info in valid_emojy:
    emo_counter += 1
    data = info.groupdict()
    emojy = data['Emojy']
    symbols = data['Surr']
    emojy_power = 0
    for letter in emojy:
        emojy_power += ord(letter)
    if emojy_power >= threshold:
        emojy_to_print.append(f'{symbols}{emojy}{symbols}')

print(f'{emo_counter} emojis found in the text. The cool ones are:')
if emojy_to_print:
    for emoticon in emojy_to_print:
        print(emoticon)
