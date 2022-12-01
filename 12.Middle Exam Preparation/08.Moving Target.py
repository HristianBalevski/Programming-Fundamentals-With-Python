sequence_of_targets = list(map(int, input().split(' ')))
data = input()

while data != 'End':
    line = data.split(' ')
    command = line[0]

    if command == 'Shoot':
        index = int(line[1])
        power = int(line[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= power
            if sequence_of_targets[index] <= 0:
                sequence_of_targets.remove(sequence_of_targets[index])
    elif command == 'Add':
        index = int(line[1])
        value = int(line[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        index = int(line[1])
        radius = int(line[2])
        if 0 > index - radius or index + radius > len(sequence_of_targets):
            print('Strike missed!')
        else:
            start_index = index - radius
            end_index = index + radius
            sequence_of_targets = [sequence_of_targets[i] for i in range(len(sequence_of_targets)) if i < start_index or i > end_index]
    data = input()
targets = list(map(str, sequence_of_targets))
print(f'|'.join(targets))
