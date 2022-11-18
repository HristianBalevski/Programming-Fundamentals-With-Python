import re

pattern = r'(@|#)[A-Za-z]{3,}\1\1[A-Za-z]{3,}\1'
text = input()
lst = []
final_lst = []
counter = 0
valid_words = re.finditer(pattern, text)
for word in valid_words:
    current_word = word.group()
    middle_index = len(current_word) // 2
    first_word = current_word[1:middle_index - 1]
    second_word = current_word[middle_index + 1: -1]
    lst.append(first_word)
    lst.append(second_word)
    counter += 1

for i in range(len(lst) - 1):
    if lst[i] == lst[i + 1][::-1]:
        final_lst.append(f'{lst[i]} <=> {lst[i + 1]}')
if not lst:
    print("No word pairs found!")
else:
    print(f'{counter} word pairs found!')
if not final_lst:
    print("No mirror words!")
else:
    print('The mirror words are:')
    final_result = [mirror_word for mirror_word in final_lst]
    print(", ".join(final_result))
