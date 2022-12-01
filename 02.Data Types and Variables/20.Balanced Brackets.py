# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
# Opening bracket – "(",
# Closing bracket – ")" or
# Random string
# Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. 
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression should be marked as unbalanced. You should print "BALANCED"
# heses are balanced and "UNBALANCED" otherwise.

number_of_lines = int(input())
brackets_counter = 0
flag = False

for number in range(number_of_lines):
    current_character = input()

    if '(' in current_character:
        brackets_counter += 1
    elif ')' in current_character:
        brackets_counter -= 1
    if brackets_counter > 1 or brackets_counter < 0:
        flag = True
        break
if flag or brackets_counter != 0:
    print('UNBALANCED')
else:
    print('BALANCED')
