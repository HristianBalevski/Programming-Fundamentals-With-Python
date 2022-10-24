initial_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    data = command.split(' ')
    current_command = data[0]
    product = data[1]

    if current_command == 'Urgent':
        if product not in initial_list:
            initial_list.insert(0, product)
    elif current_command == 'Unnecessary':
        if product in initial_list:
            initial_list.remove(product)
    elif current_command == 'Correct':
        if product in initial_list:
            new_product = data[2]
            old_product_index = initial_list.index(product)
            initial_list[old_product_index] = new_product
    elif current_command == 'Rearrange':
        if product in initial_list:
            initial_list.remove(product)
            initial_list.append(product)
print(", ".join(initial_list)