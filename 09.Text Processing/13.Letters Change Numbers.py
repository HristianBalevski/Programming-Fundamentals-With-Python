# This is the condition of the task.

'''You receive a string consisting of a number between two letters. For the given string, 
you should perform different mathematical operations to achieve a result:

First, if the letter in front of the number is:
Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)

Next, if the letter after the number is:
Uppercase: subtract its position from the resulting number (starting from 1)
Lowercase: add its position to the resulting number (starting from 1)

The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings 
keeping track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers,
it became quite hard to do it only in his mind.
He kindly asks you to write a program that performs the operations described above and sums the final results of each string.'''

# This is my solution for the task.

import re

data = input().split()

pattern = r'\d+'
front_letter = ''
number = ''
last_letter = ''
total_result = 0

for info in data:
    number = int("".join(re.findall(pattern, info)))

    for i in range(len(info)):
        if i == 0 and info[i].isupper():
            front_letter = 'upper'
            front_letter_position = ord(info[i]) - 64
        else:
            front_letter = 'lower'
            front_letter_position = ord(info[i]) - 96


        if info[-1].isupper():
            last_letter = 'upper'
            last_letter_position = ord(info[-1]) - 64
        else:
            last_letter = 'lower'
            last_letter_position = ord(info[-1]) - 96

        if front_letter == 'upper':
            result = number / front_letter_position

            if last_letter == 'upper':

                result -= last_letter_position
                total_result += result

            elif last_letter == 'lower':

                result += last_letter_position
                total_result += result

        elif front_letter == 'lower':
            result = number * front_letter_position

            if last_letter == 'upper':

                result -= last_letter_position
                total_result += result

            elif last_letter == 'lower':

                result += last_letter_position
                total_result += result
        break

print(f'{total_result:.2f}')
