number = int(input())
word = input()

original_list = []
filtered_list = []

for _ in range(number):
    some_string = input()
    original_list.append(some_string)

    if word in some_string:
        filtered_list.append(some_string)
print(original_list)
print(filtered_list)
