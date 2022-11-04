students = {}
command = input().split(":")
while len(command) > 1:
    name, id_number, course = command[0], command[1], command[2]
    if course not in students.keys(): 
        students[course] = []
    students[course].append(f"{name} - {id_number}")
    command = input().split(":")
searched_course = command[0].replace("_", " ")
for student in students[searched_course]:
    print(student)