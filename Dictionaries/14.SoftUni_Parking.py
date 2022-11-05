parking = {}
number_of_commands = int(input())

for info in range(number_of_commands):
    user_data = input().split()
    action = user_data[0]
    username = user_data[1]

    if action == 'register':
        license_number = user_data[2]
        if username not in parking:
            parking[username] = []
            parking[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif action == 'unregister':
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]
for user, number in parking.items():
    print(f"{user} => {number}")