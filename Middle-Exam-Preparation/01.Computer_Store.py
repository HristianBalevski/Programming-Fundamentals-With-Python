command = input()
prices_without_tax = 0

while command != 'special' and command != 'regular':
    amount = float(command)
    if amount < 0:
        print('Invalid price!')
        command = input()
        continue
    prices_without_tax += amount

    command = input()

if prices_without_tax == 0:
    print('Invalid order!')


taxes = prices_without_tax * 0.20
if command == 'special' and prices_without_tax > 0:
    price_with_tax = prices_without_tax + taxes
    discount = price_with_tax * 0.10
    total_price = price_with_tax - discount
    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {prices_without_tax:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$''')
if command == 'regular' and prices_without_tax > 0:
    total_price = prices_without_tax + taxes
    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {prices_without_tax:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$''')
