year = int(input())
copy_year = year
counter = 0
length = len(str(year))
flag = False
happy_year = set()

while True:
    year += 1
    counter += 1
    for num in range(length):

        last_digit = year % 10
        year = year // 10
        happy_year.add(last_digit)

    if len(happy_year) == length:
        print(copy_year + counter)
        break
    else:
        happy_year = set()
        year = copy_year + counter
