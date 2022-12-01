pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
health_capacity = int(input())
final = False


def is_valid(index, limit):
    return 0 <= index < limit


data = input().split(' ')
while data[0] != 'Retire':
    command = data[0]
    if command == 'Fire':
        index = int(data[1])
        damage = int(data[2])
        if is_valid(index, len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                final = True
                break
    elif command == 'Defend':
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if is_valid(start_index, len(pirate_ship)) and is_valid(end_index, len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    final = True
                    break
    elif command == 'Repair':
        index = int(data[1])
        health = int(data[2])
        if is_valid(index, len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > health_capacity:
                pirate_ship[index] = health_capacity
    elif command == 'Status':
        counter = 0
        for sector in pirate_ship:
            if sector < health_capacity * 0.20:
                counter += 1
        print(f'{counter} sections need repair.')

    data = input().split(' ')
if not final:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')