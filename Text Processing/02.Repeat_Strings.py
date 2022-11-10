def repeat_strings(word: str):
    text = word * len(word)
    return text


sequence_of_strings = input().split()
for i in range(len(sequence_of_strings)):
    print(repeat_strings(sequence_of_strings[i]), end="")
