data = input()
cipher = ''

for char in data:
    symbol = ord(char) + 3
    cipher += chr(symbol)
print(cipher)
