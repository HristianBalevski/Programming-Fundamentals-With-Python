list_tasks = []

while True:
    to_do_notes = input()
    
    if to_do_notes == 'End':
        break
    command = to_do_notes.split('-')
    importance = int(command[0])
    task = command[1]
    list_tasks.append((importance, task))

sorted_tasks = []
for sort_data in sorted(list_tasks):
    sorted_tasks.append(sort_data[1])

print(list(sorted_tasks))
