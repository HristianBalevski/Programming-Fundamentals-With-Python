neighborhood = list(map(int, input().split('@')))
line = input()
cupid_position = 0

while line != 'Love!':

    command = line.split(' ')
    length = int(command[1])
    cupid_position += length

    if cupid_position >= len(neighborhood):
        cupid_position = 0
    if neighborhood[cupid_position] != 0:
        neighborhood[cupid_position] -= 2
        if neighborhood[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")
    else:
        print(f"Place {cupid_position} already had Valentine's day.")
    line = input()
print(f"Cupid's last position was {cupid_position}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    missed_houses = len([num for num in neighborhood if num > 0])
    print(f"Cupid has failed {missed_houses} places.")