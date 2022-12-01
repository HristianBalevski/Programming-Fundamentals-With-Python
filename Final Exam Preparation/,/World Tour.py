text = input()
commands = input()

while commands != "Travel":
    command = commands.split(':')

    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]

        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]
            print(text)
        else:
            print(text)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print(text)
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in text:
            text = text.replace(old_string, new_string)
            print(text)
        else:
            print(text)
    commands = input()
print(f"Ready for world tour! Planned stops: {text}")
