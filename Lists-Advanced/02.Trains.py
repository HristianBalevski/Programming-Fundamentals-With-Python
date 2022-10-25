number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:

    data = input().split(' ')
    command = data[0]
    if command == 'End':
        break
    elif command == 'add':
        added_people = int(data[1])
        train[-1] += added_people
    elif command == 'insert':
        index = int(data[1])
        value = int(data[2])
        train[index] += value
    elif command == 'leave':
        index = int(data[1])
        value = int(data[2])
        train[index] -= value
print(train)