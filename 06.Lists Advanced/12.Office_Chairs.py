number_of_rooms = int(input())

chairs_left = 0
needed_chairs = 0
need_more_chairs = False

for room in range(1, number_of_rooms + 1):
    additional_information = input().split(' ')
    chairs = additional_information[0]
    visitors = additional_information[1]
    if len(chairs) > int(visitors):
        chairs_left += len(chairs) - int(visitors)
    elif len(chairs) < int(visitors):
        needed_chairs += abs(len(chairs) - int(visitors))
        print(f'{needed_chairs} more chairs needed in room {room}')
        needed_chairs = 0
        need_more_chairs = True
if not need_more_chairs:
    extra_chairs = chairs_left - needed_chairs
    print(f'Game On, {extra_chairs} free chairs left')