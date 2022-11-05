country = input().split(', ')
capitals = input().split(', ')

final_result = dict(zip(country, capitals))

for key, value in final_result.items():
    print(f'{key} -> {value}')