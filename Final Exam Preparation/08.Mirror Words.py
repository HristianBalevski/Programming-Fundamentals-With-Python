import re

text = input()
pattern = r'(@|#)(?P<Char>[A-Za-z]{3,})(\1)(\1)(?P<Copy>[A-Za-z]{3,})(\1)'

valid_pairs = re.finditer(pattern, text)
valid_pairs_count = 0
mirror_words = []

for match in valid_pairs:
    couples = match.groupdict()
    valid_pairs_count += 1
    if couples['Char'] == couples['Copy'][::-1]:
        mirror_words.append(f"{couples['Char']} <=> {couples['Copy']}")

if valid_pairs_count == 0:
    print("No word pairs found!")
else:
    print(f"{valid_pairs_count} word pairs found!")
if not mirror_words:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    print(f"{', '.join(mirror_words)}")
