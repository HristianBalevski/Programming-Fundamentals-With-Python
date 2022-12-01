line_of_integers = list(map(int, input().split(' ')))
counter_of_shoot_targets = 0
while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    if 0 <= index < len(line_of_integers):
        target_number = (line_of_integers[index])
        line_of_integers[index] = -1
        counter_of_shoot_targets += 1
        for num in range(len(line_of_integers)):
            if line_of_integers[num] > target_number and line_of_integers[num] != -1:
                line_of_integers[num] -= target_number
            elif line_of_integers[num] <= target_number and line_of_integers[num] != -1:
                line_of_integers[num] += target_number
result = list(map(str, line_of_integers))
print(f'Shot targets: {counter_of_shoot_targets} -> {" ".join(result)}')
