data = input()
bakery = {}
sold_food = 0

while data != 'Complete':
    data = data.split()
    command = data[0]
    quantity = int(data[1])
    food = data[2]

    if command == 'Receive':

        if food not in bakery and quantity > 0:
            bakery[food] = quantity
        else:
            if quantity > 0:
                bakery[food] += quantity

    elif command == 'Sell':
        if food not in bakery:
            print(f"You do not have any {food}.")

        elif bakery[food] < quantity:
            sell_counter = 0
            while bakery[food] != 0:
                bakery[food] -= 1
                sell_counter += 1
                sold_food += 1

            del bakery[food]
            print(f"There aren't enough {food}. You sold the last {sell_counter} of them.")
        else:
            bakery[food] -= quantity
            sold_food += quantity
            print(f"You sold {quantity} {food}.")
            if bakery[food] == 0:
                del bakery[food]
    data = input()
for key, value in bakery.items():
    print(f'{key}: {value}')
print(f"All sold: {sold_food} goods")
