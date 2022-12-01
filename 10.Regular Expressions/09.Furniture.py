import re

products = []
total_price = 0
pattern = r'>>(?P<Furniture>[A-Za-z]+)<<(?P<Price>\d+\.?\d+)!(?P<Quantity>\d+)\b'
data = input()

while data != 'Purchase':
    valid_information = re.finditer(pattern, data)
    for info in valid_information:
        curr_info = info.groupdict()
        furniture = curr_info['Furniture']
        price = float(curr_info['Price'])
        quantity = int(curr_info['Quantity'])
        products.append(furniture)
        total_price += price * quantity
    data = input()
print("Bought furniture:")
for item in products:
    print(item)
print(f'Total money spend: {total_price:.2f}')