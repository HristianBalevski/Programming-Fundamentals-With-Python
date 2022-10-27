sequence_of_numbers = list(map(int, input().split(', ')))
boundary = 10
printed = 0
counter = 1

for num in range(boundary):
    if len(sequence_of_numbers) == 0:
        break

    list_of_numbers = list(filter(lambda x: x <= boundary, sequence_of_numbers))
    if len(list_of_numbers) == 0:
        print(f"Group of {boundary}'s: {list_of_numbers}")
    while len(list_of_numbers) != 0:
        current_num = list_of_numbers[0]
        if printed == 0:
            print(f"Group of {boundary}'s: {list_of_numbers}")
            printed += 1
        list_of_numbers.remove(current_num)
        sequence_of_numbers.remove(current_num)
    counter += 1
    boundary = 10 * counter
    printed = 0