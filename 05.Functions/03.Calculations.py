def calculation(given_operator, first_data, second_data):
    if given_operator == 'multiply':
        result = first_data * second_data
        return result
    elif given_operator == 'divide':
        result = first_data / second_data
        return int(result)
    elif given_operator == 'add':
        result = first_data + second_data
        return result
    elif given_operator == 'subtract':
        result = first_data - second_data
        return result


operator = input()
first_number = int(input())
second_number = int(input())
print(calculation(operator, first_number, second_number))