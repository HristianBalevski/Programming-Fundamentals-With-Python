journal = input().split(', ')
data = input()

while data != 'Craft!':
    command = data.split(' - ')

    if command[0] == 'Collect':
        item = command[1]
        if item not in journal:
            journal.append(item)
    elif command[0] == 'Drop':
        point = command[1]
        if point in journal:
            journal.remove(point)
    elif command[0] == 'Combine Items':
        separate = command[1].split(':')
        old_item = separate[0]
        new_item = separate[1]
        if old_item in journal:
            index_old_item = journal.index(old_item)
            journal.insert(index_old_item + 1, new_item)
    elif command[0] == 'Renew':
        article = command[1]
        if article in journal:
            journal.remove(article)
            journal.append(article)
    data = input()
print(', '.join(journal))