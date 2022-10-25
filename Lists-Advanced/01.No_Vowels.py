text = input()
list_vowels = ['a', 'o', 'u', 'e', 'i']

no_vowels = [char for char in text if char not in list_vowels]
print("".join(no_vowels))
