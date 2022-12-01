key_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
legendary_item = ''
while legendary_item == '':
    data = input().split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1].lower()

        if material == 'shards':
            key_items['shards'] += quantity
            if key_items['shards'] >= 250:
                key_items['shards'] -= 250
                legendary_item = 'Shadowmourne'
                break
                
        elif material == 'fragments':
            key_items['fragments'] += quantity
            if key_items['fragments'] >= 250:
                key_items['fragments'] -= 250
                legendary_item = 'Valanyr'
                break
                
        elif material == 'motes':
            key_items['motes'] += quantity
            if key_items['motes'] >= 250:
                key_items['motes'] -= 250
                legendary_item = 'Dragonwrath'
                break
        else:
            if material not in junk_items:
                junk_items[material] = []
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity

print(f'{legendary_item} obtained!')
for material, quantity in key_items.items():
    print(f'{material}: {quantity}')
for junk, pcs in junk_items.items():
    print(f'{junk}: {pcs}')
