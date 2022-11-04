given_information = input().split()
bakery = {}

for index in range(0, len(given_information), 2):
    key = given_information[index]
    value = int(given_information[index + 1])
    bakery[key] = value
print(bakery)
