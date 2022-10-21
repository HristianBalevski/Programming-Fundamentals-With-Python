array_with_int = list(map(int, input().split(' ')))

while True:
    command = input()
    if command == 'end':
        break
    data = command.split(' ')
    current_command = data[0]

    if current_command == 'swap':
        index1 = int(data[1])
        index2 = int(data[2])
        array_with_int[index1], array_with_int[index2] = array_with_int[index2], array_with_int[index1]
    elif current_command == 'multiply':
        index1 = int(data[1])
        index2 = int(data[2])
        array_with_int[index1] = array_with_int[index1] * array_with_int[index2]
    elif command == 'decrease':
        array_with_int = [num - 1 for num in array_with_int]
result = list(map(str, array_with_int))
print(", ".join(result))
