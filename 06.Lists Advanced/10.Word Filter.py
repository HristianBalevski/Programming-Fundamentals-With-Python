# Using comprehension, write a program that receives some text,
# separated by space, and take only those words whose length is even.
# Print each word on a new line.

data = [even for even in input().split(' ') if len(even) % 2 == 0]
print("\n".join(data))
