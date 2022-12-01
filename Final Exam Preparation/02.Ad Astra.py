import re


pattern = r'(#|\|)(?P<Food>[A-Z a-z]+)(\1)(?P<Date>\d{2}\/\d{2}\/\d{2})(\1)(?P<Calories>\d+)(\1)'
text = input()

valid_info = re.finditer(pattern, text)
total_calories = 0
i_have_food_for = 0
all_food = []

for food in valid_info:
    my_food = food.groupdict()
    total_calories += int(my_food['Calories'])
    i_have_food_for = int(total_calories / 2000)
    all_food.append(f"Item: {my_food['Food']}, Best before: {my_food['Date']}, Nutrition: {my_food['Calories']}")
print(f"You have food to last you for: {i_have_food_for} days!")
print("\n".join(all_food))
