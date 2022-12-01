sequence_of_numbers = input().split()
list_of_numbers = []

for num in sequence_of_numbers:
    list_of_numbers.append(int(num))
print(sorted(list_of_numbers))