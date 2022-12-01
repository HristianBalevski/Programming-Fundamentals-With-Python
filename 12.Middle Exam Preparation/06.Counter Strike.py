initial_energy = int(input())
data = input()
won_battle = 0

while data != 'End of battle':
    distance = int(data)
    if initial_energy < distance:
        print(f'Not enough energy! Game ends with {won_battle} won battles and {initial_energy} energy')
        break
    else:
        initial_energy -= distance
        won_battle += 1

    if won_battle % 3 == 0:
        initial_energy += won_battle
    data = input()
if data == 'End of battle':
    print(f'Won battles: {won_battle}. Energy left: {initial_energy}')
