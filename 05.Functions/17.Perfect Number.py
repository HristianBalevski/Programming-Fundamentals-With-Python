def perfect_number(num: int):
    sum_counter = 0
    
    for digit in range(1, num):
        if num % digit == 0:
            sum_counter += digit
    if sum_counter == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))
