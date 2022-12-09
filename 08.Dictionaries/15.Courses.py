data = input()
my_dict = {}

while data != 'end':
    data = data.split(' : ')

    course = data[0]
    name = data[1]

    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append(name)

    data = input()

for key, value in my_dict.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
