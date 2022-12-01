import re

sentence = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'

occurrences = re.findall(pattern, sentence, re.IGNORECASE)
print(len(occurrences))