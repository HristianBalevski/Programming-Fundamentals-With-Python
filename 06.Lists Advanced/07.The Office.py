employees_happiness = list(map(int, input().split(' ')))
factor = int(input())
length = len(employees_happiness)
happy_people_counter = 0
total_happiness = 0
score = [num * factor for num in employees_happiness]

for num in score:
    total_happiness += num
average_happiness = total_happiness / length
filtered_numbers = list(filter(lambda x: x >= average_happiness, score))
condition = length / len(filtered_numbers)

if condition < len(filtered_numbers):
    print(f"Score: {len(filtered_numbers)}/{length}. Employees are happy!")
else:
    print(f"Score: {len(filtered_numbers)}/{length}. Employees are not happy!")
