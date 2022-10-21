people = int(input())
current_state_of_the_lift = list(map(int, input().split(' ')))
MAX_PEOPLE = 4

for index in range(len(current_state_of_the_lift)):
    while not current_state_of_the_lift[index] == MAX_PEOPLE:
        if people > 0:
            current_state_of_the_lift[index] += 1
            people -= 1
        else:
            break
all_seats = len(current_state_of_the_lift) * MAX_PEOPLE
taken_seats = sum(current_state_of_the_lift)
                                                                   
if people == 0 and all_seats - taken_seats > 0:
    print('The lift has empty spots!')
elif all_seats == taken_seats and people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
print(" ".join([str(p) for p in current_state_of_the_lift]))  
