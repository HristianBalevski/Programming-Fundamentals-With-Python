collection_of_items = input().split('|')
budget = float(input())
bought_items = []
profit = 0

for item in collection_of_items:
    data = item.split('->')
    type_of_product = data[0]
    price_of_product = data[1]

    if budget < float(price_of_product):
        continue
    if type_of_product == 'Clothes' and float(price_of_product) <= 50:
        budget -= float(price_of_product)
        new_price = float(price_of_product) + float(price_of_product) * 0.40
        bought_items.append(new_price)
        profit += new_price - float(price_of_product)
    elif type_of_product == 'Shoes' and float(price_of_product) <= 35:
        budget -= float(price_of_product)
        new_price = float(price_of_product) + float(price_of_product) * 0.40
        bought_items.append(new_price)
        profit += new_price - float(price_of_product)
    elif type_of_product == 'Accessories' and float(price_of_product) <= 20.50:
        budget -= float(price_of_product)
        new_price = float(price_of_product) + float(price_of_product) * 0.40
        bought_items.append(new_price)
        profit += new_price - float(price_of_product)
all_money = sum(bought_items) + budget
for number in bought_items:
    print(f'{number:.2f}', end=" ")
print()
print(f"Profit: {profit:.2f}")
if all_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")