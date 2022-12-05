import re

names = input().split(", ")
data = input()

pattern = r'\w+'
name = ''
points = 0
my_dict = {}

while data != 'end of race':
    valid_info = re.findall(pattern, data)
    message = "".join(valid_info)

    for i in range(len(message)):
        if message[i].isalpha():
            name += message[i]
        elif message[i].isdigit():
            points += int(message[i])
    if name in names:
        if name not in my_dict:
            my_dict[name] = points
        else:
            my_dict[name] += points
    name = ''
    points = 0
    data = input()

sorted_my_dict = sorted(my_dict.items(), key=lambda item: -item[1])
print(f"1st place: {sorted_my_dict[0][0]}")
print(f"2nd place: {sorted_my_dict[1][0]}")
print(f"3rd place: {sorted_my_dict[2][0]}")
