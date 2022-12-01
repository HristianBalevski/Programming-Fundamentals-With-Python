import re
number = int(input())

pattern = r'@([#]+)(?P<Group>[A-Z][A-Za-z0-9]{4,}[A-Z])@([#]+)'
number_of_group = ''
is_valid = False
for _ in range(number):
    data = input() 
    valid_groups = re.finditer(pattern, data)
    is_valid = False

    for group in valid_groups:
        current_group = group.group()
        is_valid = True
        for symbol in current_group:
            if symbol.isdigit():
                number_of_group += symbol
        if number_of_group:
            print(f'Product group: {number_of_group}')
            number_of_group = ''
        else:
            print('Product group: 00')

    if not is_valid:
        print('Invalid barcode')
