data = input().split(' ')
opposite_numbers = []

for num in range(len(data)):
    number = int(data[0])

    if number < 0:
        opposite_numbers.append(abs(number))
        data = data[1::]
    else:
        opposite_numbers.append(-number)
        data = data[1::]
print(opposite_numbers)