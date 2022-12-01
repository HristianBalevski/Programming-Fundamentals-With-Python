def sum_of_digits(info: str):
    even_list = []
    odd_list = []
    for num in info:
        current_number = int(num)
        if current_number % 2 == 0:
            even_list.append(current_number)
        else:
            odd_list.append(current_number)
    return f"Odd sum = {sum(odd_list)}, Even sum = {sum(even_list)}"


data = input()
print(sum_of_digits(data))