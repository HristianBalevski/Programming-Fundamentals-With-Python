# On the first line, you will receive a key (integer). 
# On the second line, you will receive n – the number of lines, which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.

key = int(input())
number_of_lines = int(input())
decrypted_word = ''

for number in range(number_of_lines):
    current_letter = input()
    current_number = ord(current_letter) + key
    decrypted_word += chr(current_number)
print(decrypted_word)