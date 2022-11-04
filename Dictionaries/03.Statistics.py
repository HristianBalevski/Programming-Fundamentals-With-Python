data = input()
food_store = {}
while data != 'statistics':
    given_information = data.split(': ')
    product = given_information[0]
    quantity = int(given_information[1])
    if product not in food_store:
        food_store[product] = quantity
    else:
        food_store[product] += quantity
    data = input()

print('Products in stock:')
for food in food_store:
    product1 = food
    print(f'- {product1}: {food_store[product1]}')
print(f'Total Products: {len(food_store)}')
print(f'Total Quantity: {sum(food_store.values())}')