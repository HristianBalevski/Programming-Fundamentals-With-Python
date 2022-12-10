data = input()
cipher = ''

for char in data:
    symbol = ord(char) + 3
    cipher += chr(symbol)
print(cipher)

# The same task solved with list comprehension.

text = input()

encrypted_text = "".join([chr(ord(char) + 3) for char in text])
print(encrypted_text)
