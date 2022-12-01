def smallest_number(one, two, three: int):
    sequence_of_numbers = [one, two, three]
    return min(sequence_of_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(smallest_number(first_number, second_number, third_number))