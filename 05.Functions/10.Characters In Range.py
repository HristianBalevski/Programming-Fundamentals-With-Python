def print_characters(first, second: str):
    symbols_list = []
    for ch in range(ord(first) + 1, ord(second)):
        symbols_list.append(chr(ch))
    return symbols_list


first_char = input()
second_char = input()
print(" ".join(print_characters(first_char, second_char)))
