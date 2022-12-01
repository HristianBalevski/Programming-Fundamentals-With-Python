message = input()
command = input()

while command != 'Reveal':
    data = command.split(":|:")
    if data[0] == 'InsertSpace':
        index = int(data[1])
        first_part = message[:index]
        second_part = message[index:]
        space = ' '
        message = first_part + space + second_part
        print(message)
    elif data[0] == 'Reverse':
        substring = data[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            new_sub = substring[::-1]
            message = message + new_sub
            print(message)
        else:
            print('error')

    elif data[0] == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
        print(message)
    command = input()
print(f"You have a new text message: {message}")
