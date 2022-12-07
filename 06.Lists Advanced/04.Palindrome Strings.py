words = input().split()
palindrome = input()

result = [word for word in words  if word == word[::-1]]

print(result)
print(f"Found palindrome {result.count(palindrome)} times")
