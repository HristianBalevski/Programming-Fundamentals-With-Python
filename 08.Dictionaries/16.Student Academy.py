number_of_iteration = int(input())
students_dictionary = {}

for iteration in range(number_of_iteration):
    name = input()
    grade = float(input())

    if name not in students_dictionary:
        students_dictionary[name] = []
    students_dictionary[name].append(grade)

for key, value in students_dictionary.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
