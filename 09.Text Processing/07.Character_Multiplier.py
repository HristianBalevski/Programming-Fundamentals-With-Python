first_part, second_part = input().split()
total_sum = 0
if len(first_part) > len(second_part):
    for index in range(len(second_part)):
        total_sum += ord(first_part[index]) * ord(second_part[index])
    for index in range(len(second_part), len(first_part)):
        total_sum += ord(first_part[index])
elif len(second_part) > len(first_part):
    for index in range(len(first_part)):
        total_sum += ord(first_part[index]) * ord(second_part[index])
    for index in range(len(first_part), len(second_part)):
        total_sum += ord(second_part[index])
else:
    for index in range(len(second_part)):
        total_sum += ord(first_part[index]) * ord(second_part[index])
print(total_sum)