given_numbers = input().split()
rounded_numbers = []

for num in range(len(given_numbers)):
    current_num = float(given_numbers[0])
    rounded_numbers.append(round(current_num))
    given_numbers = given_numbers[1:]
print(rounded_numbers)