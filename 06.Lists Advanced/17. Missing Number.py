def find_number(arr, n):
    sum1 = n * (n + 1) / 2
    sum2 = sum(arr)
    number = sum1 - sum2

    return number


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
num = my_list[-1]

print(find_number(my_list, num))
