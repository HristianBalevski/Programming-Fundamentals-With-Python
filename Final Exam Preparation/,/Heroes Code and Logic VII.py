number_of_heroes = int(input())
maximum_health = 100
maximum_mana = 200

dictionary_of_heroes = {}

for _ in range(number_of_heroes):
    data = input().split(' ')
    hero_name = data[0]
    health_points = int(data[1])
    mana_points = int(data[2])

    dictionary_of_heroes[hero_name] = {"HP": health_points, "MP": mana_points}
data = input()

while data != 'End':
    data = data.split(' - ')
    command = data[0]

    if command == 'CastSpell':
        hero_name = data[1]
        mana_points = int(data[2])
        spell_name = data[3]

        if dictionary_of_heroes[hero_name]["MP"] >= mana_points:
            dictionary_of_heroes[hero_name]['MP'] -= mana_points
            print(f"{hero_name} has successfully cast {spell_name} and now has {dictionary_of_heroes[hero_name]['MP']} MP!")
        else:

            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == 'TakeDamage':
        hero_name = data[1]
        damage = int(data[2])
        attacker = data[3]

        dictionary_of_heroes[hero_name]["HP"] -= damage
        if dictionary_of_heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dictionary_of_heroes[hero_name]['HP']} HP left!")
        else:
            del dictionary_of_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == 'Recharge':
        hero_name = data[1]
        amount = int(data[2])

        if dictionary_of_heroes[hero_name]['MP'] + amount > maximum_mana:
            counter = 0
            while dictionary_of_heroes[hero_name]['MP'] != maximum_mana:
                dictionary_of_heroes[hero_name]['MP'] += 1
                counter += 1
            print(f"{hero_name} recharged for {counter} MP!")
        else:
            dictionary_of_heroes[hero_name]['MP'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command == 'Heal':
        hero_name = data[1]
        amount = int(data[2])

        if dictionary_of_heroes[hero_name]['HP'] + amount > maximum_health:
            counter = 0
            while dictionary_of_heroes[hero_name]['HP'] != maximum_health:
                dictionary_of_heroes[hero_name]['HP'] += 1
                counter += 1
            print(f"{hero_name} healed for {counter} HP!")
        else:
            dictionary_of_heroes[hero_name]['HP'] += amount
            print(f"{hero_name} healed for {amount} HP!")
    data = input()

for hero, power in dictionary_of_heroes.items():
    print(hero)
    print(f'  HP: {power["HP"]}')
    print(f'  MP: {power["MP"]}')
