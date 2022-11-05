phonebook = {}
given_info = input()

while '-' in given_info:
    curr_info = given_info.split('-')
    name = curr_info[0]
    mobile_number = curr_info[1]

    if name not in phonebook:
        phonebook[name] = []
        phonebook[name] = mobile_number
    given_info = input()

for i in range(int(given_info)):
    names = input().split()
    for name in names:
        if name in phonebook:
            for key, value in phonebook.items():
                if key == name:
                    print(f'{key} -> {value}')
        else:
            print(f'Contact {name} does not exist.')