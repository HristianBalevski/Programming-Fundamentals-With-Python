#You will receive N – an integer, the number of snowballs being made by Tony and Andi.On the following lines, you will receive 3 inputs for each snowball:
#The weight of the snowball (integer).
#The time needed for the snowball to get to its target (integer).
#The quality of the snowball (integer)
#For each snowball, you must calculate its value by the following formula:
#(snowball_weight / snowball_time) ** snowball_quality
#In the end, you must print the highest calculated value of a snowball.

number_of_snowballs = int(input())
highest_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    needed_time = int(input())
    quality_of_the_snowball = int(input())

    current_value = (weight_of_the_snowball / needed_time) ** quality_of_the_snowball
    if current_value > highest_value:
        highest_value = current_value
        snowball_weight = weight_of_the_snowball
        snowball_time = needed_time
        snowball_quality = quality_of_the_snowball
print(f"{snowball_weight} : {snowball_time} = {int(highest_value)} ({snowball_quality})")