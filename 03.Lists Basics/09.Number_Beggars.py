data = input().split(', ')
count_of_beggars = int(input())
data_as_digits = [int(digit) for digit in data]
money_for_beggars = []
starting_index = 0

while starting_index < count_of_beggars:
    sum_of_money = 0
    for index in range(starting_index, len(data_as_digits), count_of_beggars):
        sum_of_money += data_as_digits[index]

    money_for_beggars.append(sum_of_money)
    starting_index += 1
print(money_for_beggars)