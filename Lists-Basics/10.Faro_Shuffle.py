data = input().split(' ')
count_of_faro_shuffles = int(input())

for shuffle in range(count_of_faro_shuffles):
    shuffled_deck = []
    middle_of_the_deck = len(data) // 2
    first_half = data[0:middle_of_the_deck]
    second_half = data[middle_of_the_deck:]
    for current_card in range(len(first_half)):
        shuffled_deck.append(first_half[current_card])
        shuffled_deck.append((second_half[current_card]))
    data = shuffled_deck
print(data)