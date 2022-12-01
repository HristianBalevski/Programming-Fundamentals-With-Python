info = input().split(' ')
team_A = 11
team_B = 11
players_that_left_the_game = []
flag = False

for _ in range(len(info)):
    if team_A < 7 or team_B < 7:
        flag = True
        break
    card = info[0]
    if card in players_that_left_the_game:
        info = info[1::]
        continue
    if 'A' in card:
        team_A -= 1
        players_that_left_the_game.append(card)
    elif 'B' in card:
        team_B -= 1
        players_that_left_the_game.append(card)
    info = info[1::]
print(f'Team A - {team_A}; Team B - {team_B}')
if flag:
    print('Game was terminated')
