given_string = input()

digits = []
letters = []
others = []

for i in range(len(given_string)):
    if given_string[i].isdigit():
        digits.append(given_string[i])
    elif given_string[i].isalpha():
        letters.append(given_string[i])
    else:
        others.append(given_string[i])

print("".join(digits))
print("".join(letters))
print("".join(others))
