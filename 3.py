import itertools
import os

desk = [['.' for _ in range(3)] for _ in range(3)]


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


def desk_draw(desk: list) -> None:
    print('      1       2       3\n')
    for idx, row in enumerate(desk, 1):
        print(idx, end='     ')
        print('       '.join(row), end='\n\n')


def check_desk(desk: list, symbol: str) -> bool:
    for i in range(3):
        if desk[i].count(symbol) == 3:
            return True
        elif [desk[0][i], desk[1][i], desk[2][i]].count(symbol) == 3:
            return True
        elif [desk[0][0], desk[1][1], desk[2][2]].count(symbol) == 3:
            return True
        return False


def game_question(question: str) -> None:
    while True:
        print(f"----- {question} -----", end='\n' * 2)
        answer = input('Введите да или нет - ').lower().strip()
        print()
        if answer == 'да':
            return None
        elif answer == 'нет':
            clear()
            print('До свидания!')
            exit(0)


def move(symbol: str) -> bool:
    moves = [f'{i},{j}' for i in range(1, 4) for j in range(1, 4)]
    while True:
        coords = input('Укажите координаты клетки через запятую (напр.: 1,1 или 3,3) - ').replace(' ', '')
        if coords in moves:
            i, j = map(int, coords.split(','))
            if desk[i - 1][j - 1] != '.':
                clear()
                print('Клетка уже занята. Повторите ввод.')
                return False
            break
        else:
            clear()
            print('Не верный ход. Повторите ввод.')
            return False
    clear()
    desk[i - 1][j - 1] = symbol
    return True


def game() -> None:
    player = 1
    symbol = 'X'
    while True:
        print(f'Ходит игрок {player}')
        desk_draw(desk)
        if move(symbol):
            if check_desk(desk, symbol):
                clear()
                print()
                desk_draw(desk)
                print(f'Победил игрок {player}')
                return None
            symbol = 'O' if symbol == 'X' else 'X'
            player = 2 if player == 1 else 1


if __name__ == '__main__':
    game_question('Сыграем ???')
    clear()
    while True:
        game()
        game_question('Повторим ???')
        clear()
        desk = [['.' for _ in range(3)] for _ in range(3)]
