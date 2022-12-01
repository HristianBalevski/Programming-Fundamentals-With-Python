def loading_bar(number):
    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        loading = int(number / 10)
        needed_percent = 10 - loading
        print(f"{number}% [{'%' * loading}{'.' * needed_percent}]")
        print('Still loading...')


given_number = int(input())
(loading_bar(given_number))
