import re

pattern = r'(=|\/)(?P<Name>[A-Z][A-Za-z]{2,})+(\1)'
text = input()
all_destination = []
valid_location = re.finditer(pattern, text)
travel_points = 0
for destination in valid_location:
    current_destination = destination.groupdict()
    all_destination.append(current_destination['Name'])
    travel_points += len(current_destination["Name"])
print(f'Destinations: {", ".join([country for country in all_destination])}')
print(f'Travel Points: {travel_points}')
