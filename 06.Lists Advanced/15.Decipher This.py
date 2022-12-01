secret_message = input().split()
starting_index = 0
number = ''
rest_of_the_string = ''
message = ''

for iteration in range(len(secret_message)):
    word = secret_message[starting_index]
    
    for num in word:
        if num.isdigit():
            number += num
        else:
            rest_of_the_string += num
    mid = rest_of_the_string[1:len(rest_of_the_string) - 1]
    
    if len(rest_of_the_string) < 2:
        swapped_letters = rest_of_the_string[len(rest_of_the_string) - 1] + mid
    else:
        swapped_letters = rest_of_the_string[len(rest_of_the_string) - 1] + mid + rest_of_the_string[0]        
    message += chr(int(number))
    message += swapped_letters
    starting_index += 1
    number = ''
    rest_of_the_string = ''
    print(message, end=" ")
    message = ''
