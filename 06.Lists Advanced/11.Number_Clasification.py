data = [int(number) for number in input().split(', ')]
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for num in data:
    if num >= 0:
        positive_numbers.append(str(num))
    else:
        negative_numbers.append(str(num))
    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))

print(f'Positive: {", ".join(positive_numbers)}')
print(f'Negative: {", ".join(negative_numbers)}')
print(f'Even: {", ".join(even_numbers)}')
print(f'Odd: {", ".join(odd_numbers)}')