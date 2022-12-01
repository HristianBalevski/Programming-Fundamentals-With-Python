dictionary = {}
excellent_students = {}
number_of_rows = int(input())

for num in range(number_of_rows):
    name = input()
    grade = float(input())

    if name not in dictionary:
        dictionary[name] = []
        dictionary[name] = [grade]
    else:
        dictionary[name].append(grade)
for key, value in dictionary.items():
    number_of_grades = len(value)
    sum_of_grades = sum(value)
    average_grade = sum_of_grades / number_of_grades

    if average_grade >= 4.50:
        excellent_students[key] = []
        excellent_students[key] = average_grade
for names, grades in excellent_students.items():
    print(f'{names} -> {grades:.2f}')