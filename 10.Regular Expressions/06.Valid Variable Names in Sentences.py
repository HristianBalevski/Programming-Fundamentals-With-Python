import re

pattern = r'\b_([A-Za-z0-9]+)\b'
sentence = input()

valid_words = re.findall(pattern, sentence)
print(",".join(valid_words))