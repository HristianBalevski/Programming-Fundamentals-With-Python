def total_price(product, counter):
    if product == 'coffee':
        price = 1.50 * counter
        print(f'{price:.2f}')
    elif product == 'coke':
        price = 1.40 * counter
        print(f'{price:.2f}')
    elif product == 'water':
        price = 1 * counter
        print(f'{price:.2f}')
    elif product == 'snacks':
        price = 2 * counter
        print(f'{price:.2f}')


drink = input()
quantity = int(input())
total_price(drink, quantity)