n = int(input())

dictionary = {}

for i in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]

    dictionary[piece] = {"composer": composer, "key": key}

data = input()

while data != 'Stop':
    data = data.split("|")
    command = data[0]

    if command == 'Add':
        piece = data[1]
        composer = data[2]
        key = data[3]

        if piece not in dictionary:
            dictionary[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command == 'Remove':
        piece = data[1]

        if piece in dictionary:
            del dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == 'ChangeKey':
        piece = data[1]
        new_key = data[2]

        if piece in dictionary:
            dictionary[piece]["key"] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()
for song, info in dictionary.items():
    print(f"{song} -> Composer: {info['composer']}, Key: {info['key']}")
