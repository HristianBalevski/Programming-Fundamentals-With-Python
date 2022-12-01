import re

pattern = r'(?P<Symbols>\:\:|\*\*)(?P<Emoji>[A-Z][a-z]{2,})(\1)'
digits = r'\d'
text = input()

threshold = 1
counter = 0
valid_emoji = re.finditer(pattern, text)
numbers = re.findall(digits, text)

strongest_emoji = []
power = 1
for num in numbers:
    threshold *= int(num)

for name in valid_emoji:
    emoji = name.groupdict()
    counter += 1

    for i in range(len(emoji['Emoji'])):
        power += ord(emoji['Emoji'][i])
    if power > threshold:
        strongest_emoji.append(emoji['Symbols'] + emoji['Emoji'] + emoji['Symbols'])
    power = 1
print(f'Cool threshold: {threshold}')
print(f"{counter} emojis found in the text. The cool ones are:")
if strongest_emoji:
    for info in strongest_emoji:
        print(info)
