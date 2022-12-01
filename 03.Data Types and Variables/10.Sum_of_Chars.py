#Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter per line. Print the total sum in the following format: "The sum equals: {total_sum}".

number_of_lines = int(input())
total_sum = 0

for number in range(number_of_lines):
    current_letter = input()
    total_sum += ord(current_letter)
print(f'The sum equals: {total_sum}')