given_information = input().split()
searched_products = input().split()
my_dictionary = {}
for index in range(0, len(given_information), 2):
    product = given_information[index]
    quantity = given_information[index + 1]
    my_dictionary[product] = quantity

for looking_for in searched_products:
    if looking_for not in given_information:
        print(f"Sorry, we don't have {looking_for}")
    else:
        print(f"We have {my_dictionary[looking_for]} of {looking_for} left")