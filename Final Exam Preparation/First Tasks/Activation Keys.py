raw_activation_key = input()
data = input()

while data != 'Generate':
    data = data.split('>>>')
    command = data[0]

    if command == 'Contains':
        substring = data[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        action = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        first_part = raw_activation_key[:start_index]
        to_change = raw_activation_key[start_index:end_index]
        second_part = raw_activation_key[end_index:]

        if action == 'Upper':
            raw_activation_key = first_part + to_change.upper() + second_part
            print(raw_activation_key)
        elif action == 'Lower':
            raw_activation_key = first_part + to_change.lower() + second_part
            print(raw_activation_key)

    elif command == 'Slice':
        first_index = int(data[1])
        second_index = int(data[2])
        first_part = raw_activation_key[:first_index]
        to_delete = raw_activation_key[first_index:second_index]
        second_part = raw_activation_key[second_index:]
        raw_activation_key = first_part + second_part
        print(raw_activation_key)
    data = input()
print(f'Your activation key is: {raw_activation_key}')
