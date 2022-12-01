given_string = list(map(int, input().split(', ')))
indices = [num for num in range(len(given_string)) if given_string[num] % 2 == 0]
print(indices)
