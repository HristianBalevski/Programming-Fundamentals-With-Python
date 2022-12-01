encrypted_message = input()
data = input()

while data != 'Decode':
    command = data.split('|')

    if command[0] == 'Move':
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] +  encrypted_message[:number_of_letters]
    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]

        while substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)
    data = input()
print(f"The decrypted message is: {encrypted_message}")
