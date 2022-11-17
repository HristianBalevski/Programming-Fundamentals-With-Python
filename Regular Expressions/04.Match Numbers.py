import re

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
text = input()

valid_numbers = re.finditer(pattern, text)
for number in valid_numbers:
    current_number = number.group()
    print(current_number, end=" ")