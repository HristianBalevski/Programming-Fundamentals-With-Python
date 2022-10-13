#Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons. The input holds two lines: the number of people N and the capacity P of the elevator.

number_of_people = int(input())
capacity_of_elevator = int(input())

courses_counter = int(number_of_people / capacity_of_elevator)

if number_of_people % capacity_of_elevator == 0:
    print(courses_counter)
else:
    print(courses_counter + 1)