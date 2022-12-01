#Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

given_number = int(input())

for first_letter in range(given_number):
    for second_letter in range(given_number):
        for third_letter in range(given_number):
            print(f'{chr(first_letter + 97)}{chr(second_letter + 97)}{chr(third_letter + 97)}')
