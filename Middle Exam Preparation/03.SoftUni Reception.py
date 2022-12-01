first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
time_counter = 0

while students_count > 0:
    students_count -= first_employee + second_employee + third_employee
    time_counter += 1

    if time_counter % 4 == 0:
        time_counter += 1
        continue
print(f'Time needed: {time_counter}h.')
