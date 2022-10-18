level_of_fire = input().split('#')
amount_of_water = int(input())
effort = 0
total_fire = 0
print('Cells:')

for fire in level_of_fire:
    fire_info = fire.split(' = ')
    power_of_fire = fire_info[0]
    value_of_fire = int(fire_info[1])
    if amount_of_water == 0:
        break
    if amount_of_water < value_of_fire:
        continue

    if power_of_fire == 'High' and 81 <= value_of_fire <= 125:
        amount_of_water -= value_of_fire
        effort += value_of_fire * 0.25
        total_fire += value_of_fire
        print(f'- {value_of_fire}')
    elif power_of_fire == 'Medium' and 51 <= value_of_fire <= 80:
        amount_of_water -= value_of_fire
        effort += value_of_fire * 0.25
        total_fire += value_of_fire
        print(f'- {value_of_fire}')
    elif power_of_fire == 'Low' and 1 <= value_of_fire <= 50:
        amount_of_water -= value_of_fire
        effort += value_of_fire * 0.25
        total_fire += value_of_fire
        print(f'- {value_of_fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')