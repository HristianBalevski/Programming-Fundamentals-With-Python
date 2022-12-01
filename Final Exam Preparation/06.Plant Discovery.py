number = int(input())

plant_dict = {}

for i in range(number):
    data = input().split('<->')
    name_plant = data[0]
    rarity = int(data[1])

    if name_plant not in plant_dict:
        plant_dict[name_plant] = {'rarity': rarity, 'rating': []}
    else:
        plant_dict[name_plant]['rarity'] += rarity

while True:
    command = input().split(': ')

    if command[0] == 'Exhibition':
        break

    data = command[1].split(' - ')
    type_of_command = command[0]
    plant = data[0]

    if plant not in plant_dict:
        print('error')
        continue

    if type_of_command == 'Rate':
        rating = int(data[1])
        plant_dict[plant]['rating'].append(rating)

    elif type_of_command == 'Update':
        new_rarity = int(data[1])
        plant_dict[plant]['rarity'] = new_rarity

    elif type_of_command == 'Reset':
        plant_dict[plant]['rating'].clear()

print('Plants for the exhibition:')
for info in plant_dict:
    if len(plant_dict[info]['rating']) > 0 and sum(plant_dict[info]['rating']) > 0:
        average = sum(plant_dict[info]['rating']) / len(plant_dict[info]['rating'])
        print(f"- {info}; Rarity: {plant_dict[info]['rarity']}; Rating: {average:.2f}")
    else:
        average = 0
        rarity = plant_dict[info]['rarity']
        print(f"- {info}; Rarity: {rarity}; Rating: {average:.2f}")
