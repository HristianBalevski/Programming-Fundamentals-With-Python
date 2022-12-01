# On the first line, you will receive a sequence of numbers separated by a single space. On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the sequence.
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index).
# When you find a char, you should add it to the message and remove it from the string. 
# It means that for the following index, the text will be with one character less.

# Example

# Input
# 9992 562 8933
# This is some message for you

# Output
# hey

# Input
# 2 122 1123 1321 9 17211
# 87j973u59dg37e725!

# Output
# judge!

sequence_of_numbers = input().split(' ')
line = input()
message = ''

for i in range(len(sequence_of_numbers)):
    the_sum = 0
    res = 0
    data = sequence_of_numbers[i]
    for x in data:
        the_sum += int(x)
    if the_sum >= len(line):
        res = the_sum - len(line)
        message += line[res]
        line = line[0: res:] + line[res + 1::]
    else:
        message += line[the_sum]
        line = line[0: the_sum:] + line[the_sum + 1::]
print(message)
