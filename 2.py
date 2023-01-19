import os
import random
import time


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


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


def game():
    candies = 2021
    max_move = 28
    players = [input(f'Введите имя игрока {i} - ') for i in range(1, 3)]
    print('Жеребьевка...', end='')
    time.sleep(3)
    print('\r', end='')
    idx = random.randint(0, 1)
    while candies > 0:
        print(f'Ходит  {players[idx]}.')
        print(f'Осталось {candies} конфет(ы).')
        chunk = int(input('Сколько конфет забрать: '))
        if 0 < chunk < 29:
            candies -= chunk
            if candies < 1:
                break
            else:
                idx = 1 if idx == 0 else 0
        else:
            print('Можно забрать от 1 до 28 конфет. Повторите.')
    print(f'Выиграл(а) {players[idx]} ')


if __name__ == '__main__':
    game()
