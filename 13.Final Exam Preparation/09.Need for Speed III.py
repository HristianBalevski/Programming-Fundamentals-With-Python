number_of_cars = int(input())

dict_cars = {}

for i in range(number_of_cars):
    info = input().split("|")
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])

    dict_cars[car] = {'Mileage': mileage, 'Fuel': fuel}

while True:
    data = input().split(" : ")
    command = data[0]

    if command == 'Stop':
        break
    car = data[1]

    if command == 'Drive':
        distance = int(data[2])
        fuel = int(data[3])

        if dict_cars[car]['Fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            dict_cars[car]['Mileage'] += distance
            dict_cars[car]['Fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if dict_cars[car]['Mileage'] >= 100000:
                del dict_cars[car]
                print(f"Time to sell the {car}!")

    elif command == 'Refuel':
        fuel = int(data[2])
        counter = 0

        if dict_cars[car]['Fuel'] + fuel > 75:
            while dict_cars[car]['Fuel'] != 75:
                dict_cars[car]['Fuel'] += 1
                counter += 1
            print(f"{car} refueled with {counter} liters")
        else:
            dict_cars[car]['Fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        kilometers = int(data[2])

        dict_cars[car]['Mileage'] -= kilometers

        if dict_cars[car]['Mileage'] < 10000:
            dict_cars[car]['Mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

for vehicle, information in dict_cars.items():
    print(f"{vehicle} -> Mileage: {information['Mileage']} kms, Fuel in the tank: {information['Fuel']} lt.")
