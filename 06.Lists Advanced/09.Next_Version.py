def next_version(one, two, three):
    if three < 9:
        three += 1
    else:
        three = 0
        two += 1
        if two > 9:
            two = 0
            one += 1
    return f'{one}.{two}.{three}'


version = [int(num) for num in input().split('.')]
number_one = version[0]
number_two = version[1]
number_three = version[2]
print(next_version(number_one, number_two, number_three))