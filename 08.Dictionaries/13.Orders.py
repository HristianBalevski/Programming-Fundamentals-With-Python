orders = {}
command = input()

while command != 'buy':
    product = command.split()[0]
    price = float(command.split()[1])
    quantity = int(command.split()[2])

    if product not in orders:
        orders[product] = [quantity]
        orders[product] += [price]
    else:
        orders[product][0] += quantity
        if price != orders[product][1]:
            del orders[product][1]
            orders[product] += [price]
    command = input()

for name, pcs in orders.items():
    total_price = pcs[0] * pcs[1]
    print(f'{name} -> {total_price:.2f}')