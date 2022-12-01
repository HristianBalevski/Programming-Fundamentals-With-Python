numbers = input().split(' ')
killed = int(input())
output = []
counter = 0
current_index = 0

while len(numbers) > 0:
    counter += 1
    
    if counter % killed == 0:
        output.append(numbers[current_index])
        numbers.pop(current_index)
    else:
        current_index += 1
        
    if current_index >= len(numbers):
        current_index = 0
print(str(output).replace(' ', '').replace('\'', ''))
