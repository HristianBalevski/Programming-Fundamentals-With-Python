treasure = {}
command = input()
counter = 0
commodity = ''
quantity = 0

while command != 'stop':
    counter += 1
    if counter % 2 != 0:
        commodity = command
        if commodity not in treasure:
            treasure[commodity] = []
    else:
        quantity = int(command)
        if treasure[commodity]:
            treasure[commodity] += quantity
        else:
            treasure[commodity] = quantity
    command = input()

for key, value in treasure.items():
    print(f'{key} -> {value}')
