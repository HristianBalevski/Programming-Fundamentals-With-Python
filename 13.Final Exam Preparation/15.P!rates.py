info = input()
pirates_dict = {}

while info != 'Sail':
    info = info.split("||")

    city = info[0]
    population = int(info[1])
    gold = int(info[2])

    if city not in pirates_dict:
        pirates_dict[city] = {'Population': population, 'Gold': gold}
    else:
        pirates_dict[city]['Population'] += population
        pirates_dict[city]['Gold'] += gold
    info = input()

info = input()

while info != 'End':
    info = info.split('=>')
    event = info[0]

    if event == 'Plunder':
        town = info[1]
        people = int(info[2])
        money = int(info[3])

        pirates_dict[town]['Population'] -= people
        pirates_dict[town]['Gold'] -= money
        print(f"{town} plundered! {money} gold stolen, {people} citizens killed.")

        if pirates_dict[town]['Population'] == 0 or pirates_dict[town]['Gold'] == 0:
            del pirates_dict[town]
            print(f"{town} has been wiped off the map!")
    elif event == 'Prosper':
        town = info[1]
        money = int(info[2])

        if money < 0:
            print("Gold added cannot be a negative number!")
        else:
            pirates_dict[town]['Gold'] += money
            print(f"{money} gold added to the city treasury. {town} now has {pirates_dict[town]['Gold']} gold.")
    info = input()

if pirates_dict:
    print(f"Ahoy, Captain! There are {len(pirates_dict)} wealthy settlements to go to:")
    for town, data in pirates_dict.items():
        print(f'{town} -> Population: {data["Population"]} citizens, Gold: {data["Gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
