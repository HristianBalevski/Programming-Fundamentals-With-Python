import re

pattern = r'(=|\/)(?P<Destination>[A-Z][A-Za-z]{2,})(\1)'
text = input()

valid_location = re.finditer(pattern, text)
my_destination = []
travel_points = 0

for destination in valid_location:
    current_destination = destination.groupdict()
    my_destination.append(current_destination['Destination'])
    travel_points += len(current_destination['Destination'])

print(f'Destinations: {", ".join(my_destination)}')
print(f"Travel Points: {travel_points}")
