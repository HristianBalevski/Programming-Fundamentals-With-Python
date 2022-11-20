import re

pattern = '\d+'
text = input()
while text:
    data = re.findall(pattern, text)
    if data:
        print(" ".join(data), end=" ")
    text = input()