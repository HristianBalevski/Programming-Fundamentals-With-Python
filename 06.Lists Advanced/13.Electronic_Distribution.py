number_of_electrons = int(input())
copy_number_of_electrons = number_of_electrons
maximum_number = 0
filled_shells = []

for electron in range(1, number_of_electrons + 1):
    maximum_number = 2 * electron ** 2
    if copy_number_of_electrons < maximum_number:
        filled_shells.append(copy_number_of_electrons)
        break
    else:
        filled_shells.append(maximum_number)
    copy_number_of_electrons -= maximum_number
    if copy_number_of_electrons == 0:
        break
print(filled_shells)