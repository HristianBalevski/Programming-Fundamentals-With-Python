data = input()
my_dictionary = {}

while data != 'End':
    data = data.split(' -> ')

    company_name = data[0]
    employee_id = data[1]

    if company_name not in my_dictionary:
        my_dictionary[company_name] = [employee_id]
    else:
        if employee_id not in my_dictionary[company_name]:
            my_dictionary[company_name].append(employee_id)
    data = input()

for key, value in my_dictionary.items():
    print(key)
    for index in range(len(value)):
        print(f'-- {value[index]}')
