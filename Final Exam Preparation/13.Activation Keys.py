key = input()
data = input()

while data != "Generate":
    data = data.split(">>>")

    command = data[0]

    if command == "Contains":
        substring = data[1]

        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
            
    elif command == "Flip":
        size = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        first_part = key[:start_index]
        second_part = key[end_index:]
        to_change = key[start_index:end_index]
        if size == 'Upper':
            to_change = to_change.upper()
        else:
            to_change = to_change.lower()
        key = first_part + to_change + second_part
        print(key)
        
    elif command == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        first_part = key[:start_index]
        second_part = key[end_index:]
        to_delete = key[start_index:end_index]
        key = first_part + second_part
        print(key)
    data = input()
print(f"Your activation key is: {key}")
