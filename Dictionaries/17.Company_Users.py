company_users = {}
command = input()

while command != 'End':
    information = command.split(' -> ')
    company_name = information[0]
    employee_id = information[1]

    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)
    command = input()

for company, employee in company_users.items():
    print(company)
    final_data = '\n-- '.join(employee)
    print(f"-- {final_data}")