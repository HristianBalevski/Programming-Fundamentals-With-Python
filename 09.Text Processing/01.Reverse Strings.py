def reverse_strings(word: str):

    reversed_word = word[::-1]
    return f'{word} = {reversed_word}'


given_words = input().split()
while given_words[0] != 'end':
    print(reverse_strings(given_words[0]))
    given_words = input().split()
