def grade(num):
    if 2 <= num <= 2.99:
        print('Fail')
    elif 3 <= num <= 3.49:
        print('Poor')
    elif 3.50 <= num <= 4.49:
        print('Good')
    elif 4.50 <= num <= 5.49:
        print('Very Good')
    elif 5.50 <= num <= 6.00:
        print('Excellent')


data = float(input())
grade(data)