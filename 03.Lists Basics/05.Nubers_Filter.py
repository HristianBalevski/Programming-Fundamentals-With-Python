number = int(input())

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []


for _ in range(number):
    current_number = int(input())

    if current_number % 2 == 0:
        even_numbers.append(current_number)
    if current_number % 2 != 0:
        odd_numbers.append(current_number)
    if current_number < 0:
        negative_numbers.append(current_number)
    if current_number >= 0:
        positive_numbers.append(current_number)
command = input()

if command == 'even':
    print(even_numbers)
elif command == 'odd':
    print(odd_numbers)
elif command == 'negative':
    print(negative_numbers)
elif command == 'positive':
    print(positive_numbers)
