# Создайте программу для игры в 'Крестики-нолики'

from random import randint as r
from os import system, name

list = [[0 for i in range(3)] for j in range(3)]

def drawGameBoard(isFirst, player):
    clear()
    if isFirst:
        print('КРЕСТИКИ-НОЛИКИ')
    else:
        print(f'Состояние доски после хода {p(player)}:')
    print('    1   2   3')
    print('  \u250F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u2513')
    print(f'А \u2503 {c(list[0][0])} \u2503 {c(list[0][1])} \u2503 {c(list[0][2])} \u2503')
    print('  \u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B')
    print(f'Б \u2503 {c(list[1][0])} \u2503 {c(list[1][1])} \u2503 {c(list[1][2])} \u2503')
    print('  \u2523\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u252B')
    print(f'В \u2503 {c(list[2][0])} \u2503 {c(list[2][1])} \u2503 {c(list[2][2])} \u2503')
    print('  \u2517\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u251B')

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def c(item):
    # print(item)
    if item == 0:
        return ' '
    elif item == 1:
        return 'x'
    return 'o'

def getResult():
    if isAllFill():
        return -1
    for p in range (1, 3):
        if line(p) or col(p) or diag(p):
            return p
    return 0

def isAllFill():
    for x in range(0, 3):
        for y in range(0, 3):
            if list[x][y] == 0:
                return False
    return True

def line(p):
    for x in range(0, 3):
        if list[0][x] == p and list[1][x] == p and list[2][x] == p:
            return True
    return False

def col(p):
    for y in range(0, 3):
        if list[y][0] == p and list[y][1] == p and list[y][2] == p:
            return True
    return False

def diag(p):
    return list[0][0] == p and list[1][1] == p and list[2][2] == p \
        or list[2][0] == p and list[1][1] == p and list[0][2] == p

def changePlayer(player):
    if player == 1:
        return 2
    else:
        return 1

def p(player):
    if player == 1:
        return 'Х'
    return 'О'

def getMove(player):
    while True:
        x = -1
        y = -1
        move = str(input(f'Игрок {p(player)}, сделайте ход (например, А2): ').lower())
        if len(move) >= 2:
            match move[0]:
                case 'а':
                    x = 0
                case 'б':
                    x = 1
                case 'в':
                    x = 2
                case _:
                    x = -1
            y = int(move[1]) - 1
        if x != -1 and y != -1 and list[x][y] == 0:
            list[x][y] = player
            return
    
player = r(1, 2)
drawGameBoard(True, player)
result = 0
print(f'Первым ходит игрок {p(player)}!')
while result == 0:
    getMove(player)
    drawGameBoard(False, player)
    result = getResult()
    player = changePlayer(player)

if result < 0:
    print('Победила дружба!')
else:
    print(f'Победил игрок {p(result)}')