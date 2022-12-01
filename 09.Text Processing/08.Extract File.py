data = input().split('\\')
data = data[-1].split('.')

template = data[0]
extension = data[1]

print(f'File name: {template}')
print(f'File extension: {extension}')
