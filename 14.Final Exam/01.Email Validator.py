given_email = input()
data = input()

while data != 'Complete':
    if data == 'GetUsername':
        substring = ''

        if '@' in given_email:
            for char in given_email:
                if char != '@':
                    substring += char
                else:
                    print(substring)
                    break
        else:
            print(f"The email {given_email} doesn't contain the @ symbol.")

    elif data == 'Encrypt':
        encrypted_message = []
        for char in given_email:
            encrypted_message.append(str(ord(char)))
        print(" ".join(encrypted_message))
    else:
        data = data.split()

    if data[1] == 'Upper':
        given_email =  given_email.upper()
        print(given_email)

    elif data[1] == 'Lower':
        given_email = given_email.lower()
        print(given_email)

    elif data[0] == 'GetDomain':
        count = int(data[1])
        to_print = ''
        counter = 0
        for i in range(count):
            counter += 1
            to_print +=  given_email[::-1][i]
            if count == counter:
                print(to_print[::-1])

    elif data[0] == 'Replace':
        char = data[1]

        given_email = given_email.replace(char, '-')
        print(given_email)

    data = input()
