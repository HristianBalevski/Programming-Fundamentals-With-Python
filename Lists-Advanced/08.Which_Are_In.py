# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line

def substrings(one, two):
    list_substrings = []
    for word in one:
        for second_word in two:
            if word in second_word:
                list_substrings.append(word)
                break
    return list_substrings


first_string = input().split(', ')
second_string = input().split(', ')
print(substrings(first_string, second_string))