import re

number = int(input())
pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([a-z]{5,}[0-9]+)P@\$'
counter = 0

for i in range(number):
    data = input()

    valid_registration = re.findall(pattern, data)

    if len(valid_registration) == 0:
        print("Invalid username or password")
    else:
        for reg in valid_registration:
            counter += 1
            print("Registration was successful")
            print(f"Username: {reg[0]}, Password: {reg[1]}")
print(f"Successful registrations: {counter}")
