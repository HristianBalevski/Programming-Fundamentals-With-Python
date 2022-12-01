data = input().split('|')
health = 100
bitcoins = 0
best_room = 0
last_bitcoins = 0
previous_health = 0

for index in range(len(data)):
    info = data[index].split(' ')
    command = info[0]
    value = int(info[1])

    if command == "potion":
        health += value
        if health > 100:
            health = 100
            print(f"You healed for {health - previous_health} hp.")
        else:
            print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += value
        if value > last_bitcoins:
            last_bitcoins = value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            if index == 0:
                best_room = 1
            else:
                best_room = index + 1
            print(f"Best room: {best_room}")
            break
    previous_health = health
if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")