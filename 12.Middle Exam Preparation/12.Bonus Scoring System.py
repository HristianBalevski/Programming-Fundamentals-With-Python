from math import ceil
number_of_the_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
student_with_maximum_bonus = 0
attendance = 0

for student in range(1, number_of_the_students + 1):

    attendance_of_each_student = int(input())
    total_bonus = attendance_of_each_student / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > student_with_maximum_bonus:
        student_with_maximum_bonus = total_bonus
        attendance = attendance_of_each_student

print(f'Max Bonus: {ceil(student_with_maximum_bonus)}.')
print(f'The student has attended {attendance} lectures.')
