my_stops = input()
data = input()

while data != 'Travel':
    info = data.split(':')

    if info[0] == 'Add Stop':
        index = int(info[1])
        text = info[2]

        if 0 <= index < len(my_stops):
            my_stops = my_stops[:index] + text + my_stops[index:]
            print(my_stops)
        else:
            print(my_stops)
    elif info[0] == 'Remove Stop':
        start_index = int(info[1])
        end_index = int(info[2])

        if 0 <= start_index <= len(my_stops) and start_index <= end_index <= len(my_stops):
            my_stops = my_stops[:start_index] + my_stops[end_index + 1:]
            print(my_stops)
        else:
            print(my_stops)
    elif info[0] == 'Switch':
        old_string = info[1]
        new_string = info[2]
        if old_string in my_stops:
            while old_string in my_stops:
                my_stops = my_stops.replace(old_string, new_string)
            print(my_stops)
        else:
            print(my_stops)
    data = input()
print(f"Ready for world tour! Planned stops: {my_stops}")
