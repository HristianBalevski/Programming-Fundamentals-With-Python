numbers = input().split(' ')
numbers_for_remove = int(input())
output = []

for num in range(len(numbers)):
    current_number = numbers[0]
    output.append(int(current_number))
    numbers = numbers[1::]

for _ in range(numbers_for_remove):
    output.remove(min(output))
print(', '.join(map(str, output)))
