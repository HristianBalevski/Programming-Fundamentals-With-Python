number_of_cars = int(input())

car_dictionary = {}

for _ in range(number_of_cars):
    data = input().split("|")

    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    car_dictionary[car] = {"mileage": mileage, "fuel": fuel}

data = input()

while data != 'Stop':

    data = data.split(" : ")
    command = data[0]

    if command == 'Drive':
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])

        if car_dictionary[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_dictionary[car]["mileage"] += distance
            car_dictionary[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_dictionary[car]["mileage"] >= 100000:
                del car_dictionary[car]
                print(f"Time to sell the {car}!")

    elif command == 'Refuel':
        car = data[1]
        fuel = int(data[2])

        if car_dictionary[car]["fuel"] + fuel > 75:
            counter = 0
            while car_dictionary[car]["fuel"] != 75:
                car_dictionary[car]["fuel"] += 1
                counter += 1
            print(f"{car} refueled with {counter} liters")
        else:
            car_dictionary[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif command == 'Revert':
        car = data[1]
        kilometers = int(data[2])

        car_dictionary[car]["mileage"] -= kilometers
        if car_dictionary[car]["mileage"] < 10000:
            car_dictionary[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    data = input()

for vehicle, info in car_dictionary.items():
    print(f"{vehicle} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")
