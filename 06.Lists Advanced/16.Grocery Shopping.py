products_list = input().split("|")
data = input()

while data != 'Shop!':
    data = data.split('%')
    command = data[0]

    if command == 'Important':
        product = data[1]

        if product in products_list:
            products_list.remove(product)
            products_list.insert(0, product)
        else:
            products_list.insert(0, product)

    elif command == 'Add':
        product = data[1]

        if product not in products_list:
            products_list.append(product)
        else:
            print("The product is already in the list.")

    elif command == 'Swap':
        first_item = data[1]
        second_item = data[2]

        if first_item in products_list and second_item in products_list:
            first_index = products_list.index(first_item)
            second_index = products_list.index(second_item)
            products_list[first_index], products_list[second_index] = products_list[second_index], products_list[first_index]

        if first_item not in products_list:
            print(f"Product {first_item} missing!")

        elif second_item not in products_list:
            print(f"Product {second_item} missing!")

    elif command == 'Remove':
        product = data[1]

        if product in products_list:
            products_list.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    elif command == 'Reversed:':
        products_list = products_list[::-1]

    data = input()

counter = 1
for p in products_list:
    print(f'{counter}. {p}')
    counter += 1
