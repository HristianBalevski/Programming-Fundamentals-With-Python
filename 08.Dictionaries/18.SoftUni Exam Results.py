exam_results = {}
submissions = {}
command = input()

while command != 'exam finished':
    data = command.split('-')
    student_name = data[0]
    program_language = data[1]
    
    if program_language not in submissions and program_language != 'banned':
        submissions[program_language] = 1
    else:
        if program_language != 'banned':
            submissions[program_language] += 1
            
    if program_language == 'banned':
        del exam_results[student_name]
        command = input()
        continue
    points = int(data[2])

    if student_name not in exam_results:
        exam_results[student_name] = []
        exam_results[student_name] = [program_language, points]
        
    elif student_name in exam_results and program_language in exam_results[student_name]:
        if exam_results[student_name][1] < points:
            exam_results[student_name][1] = points
            
    elif student_name in exam_results and program_language not in exam_results[student_name]:
        exam_results[student_name] += [program_language, points]
    command = input()

print('Results:')
for username, point in exam_results.items():
    print(f'{username} | {point[1]}')
print('Submissions:')

for languages, submissions_count in submissions.items():
    print(f'{languages} - {submissions_count}')
