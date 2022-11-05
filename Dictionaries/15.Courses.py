student_dictionary = {}
command = input()

while command != 'end':
    data = command.split(" : ")
    course_name = data[0]
    student_name = data[1]

    if course_name not in student_dictionary:
        student_dictionary[course_name] = []
        student_dictionary[course_name] = [student_name]
    else:
        student_dictionary[course_name].append(student_name)
    command = input()

for course, student in student_dictionary.items():
    print(f"{course}: {len(student)}")
    result = '\n-- '.join(student)
    print(f"-- {result}")