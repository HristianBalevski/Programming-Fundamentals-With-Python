data = input()
my_orders = {}

while data != 'buy':
    data = data.split()
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in my_orders:
        my_orders[product] = {'Price': price, 'Quantity': quantity}
    else:
        my_orders[product]['Quantity'] += quantity
        if my_orders[product]['Price'] != price:
            my_orders[product]['Price'] = price
    data = input()

for key, value in my_orders.items():
    print(f"{key} -> {value['Price'] * value['Quantity']:.2f}")
