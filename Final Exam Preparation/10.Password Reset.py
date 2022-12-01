text = input()
data = input()

while data != 'Done':
    data = data.split(" ")
    command = data[0]

    if command == "TakeOdd":
        text = "".join([text[i] for i in range(len(text)) if i % 2 != 0])
        print(text)
    elif command == 'Cut':
        index = int(data[1])
        length = int(data[2])
        text = "".join([text[i] for i in range(len(text)) if i < index or i >= index + length])
        print(text)

    elif command == 'Substitute':
        substring = data[1]
        substitute = data[2]

        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")
    data = input()
print(f"Your password is: {text}")
