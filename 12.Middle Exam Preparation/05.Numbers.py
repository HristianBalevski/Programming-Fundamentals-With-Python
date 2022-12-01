sequence_of_integers = list(map(int, input().split(' ')))
total_sum = sum(sequence_of_integers)
average = total_sum // len(sequence_of_integers)
greater_numbers = []
limit = 5
sequence_of_integers.sort(reverse=True)
for num in sequence_of_integers:
    if num > average and len(greater_numbers) != limit:
        greater_numbers.append(num)
if len(greater_numbers) == 0:
    print('No')
else:
    greater_numbers = list(map(str, greater_numbers))
    print(" ".join(greater_numbers))
