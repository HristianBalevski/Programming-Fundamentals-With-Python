sequence_of_numbers = input().split()
even_nums = []
for num in sequence_of_numbers:
    even_nums.append(int(num))
result = filter(lambda x: x % 2 == 0, even_nums)
print(list(result))
