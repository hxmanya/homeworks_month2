
from decouple import config
from random import randint



if_new = True
initial_capital = config('INITIAL_CAPITAL', cast=int)
list_1 = list(map(int, config('RANGE').split(' ')))
attempts = config('ATTEMPTS', cast=int)
capital = 0

def get_hidden_number():
    hidden_number = randint(list_1[0], list_1[1])
    return hidden_number

def make_bet(max_bet):
    while True:
        try:
            new_bet = int(input(f'Введите вашу ставку(не больше {max_bet}): '))
            if not 0 < new_bet <= max_bet:
                raise ValueError
        except ValueError:
            print(f'Введите целое число от 0 до {max_bet}!')
        except TypeError:
            print(f'Введите целое число от 0 до {max_bet}!')
        else:
            break
    return new_bet


def guess_number():
    while True:
        try:
            guessed_number = int(input('Введите ваше число: '))
            if not list_1[0] <= guessed_number <= list_1[1]:
                raise ValueError
        except ValueError:
            print('Введите целое число от 1 до 10!')
        except TypeError:
            print('Введите целое число от 1 до 10!')
        else:
            break
    return guessed_number

def start_game():
    global if_new
    global capital
    if if_new:
        capital = initial_capital
        print(f'Ваш начальный капитал: {initial_capital}')
    else:
        print(f'Ваш капитал: {capital}')


    hidden_number = get_hidden_number()
    print('Программа выбрала число от 1 до 10!\n'
            'Попробуте его отгадать!')


    print(f'У вас {attempts} попыток!')

    bet = make_bet(capital)
    for i in range(attempts):
        guessed_number = guess_number()
        if guessed_number == hidden_number:
            print('Поздравляю! Вы угадали число!')
            capital += bet
            print(f'Ваш капитал составляет: {capital}')
            break
        print(f'Не угадали!(попыток осталось {attempts - i - 1})')
        if i == attempts - 1:
            print(f'Увы, вы не угадали число с {attempts} попыток! Вы проиграли!')
            capital -= bet
            print(f'Ваш капитал составляет: {capital}')

    if capital != 0:
        while True:
            try:
                print('Выберите одну из последующих опций:')
                print('1. Продолжить играть.')
                print('2. Начать заново.')
                print('3. Завершить игру.')
                if_continue = int(input('Введите номер: '))
                if not 1 <= if_continue <= 3:
                    raise ValueError
            except ValueError:
                print('Введите целое число(1, 2 или 3)!')
            except TypeError:
                print('Введите целое число(1, 2 или 3)!')
            else:
                break
        if if_continue == 1:
            if_new = False
            print('Продолжаем игру!')
            start_game()
        elif if_continue == 2:
            if_new = True
            print('Начинаем заново!')
            start_game()
        else:
                print('Игра закончена!')
    else:
        print('У вас недостаточно капитала для ставки!')
        while True:
            try:
                print('Выберите одну из последующих опций:')
                print('1. Начать заново.')
                print('2. Завершить игру.')
                if_continue = int(input('Введите номер: '))
                if not 1 <= if_continue <= 2:
                    raise ValueError
            except ValueError:
                print('Введите целое число(1 или 2)!')
            except TypeError:
                print('Введите целое число(1 или 2)!')
            else:
                break
        if if_continue == 1:
            if_new = True
            print('Начинаем заново!')
            start_game()
        else:
            print('Игра закончена!')





if __name__ == '__main__':
    start_game()




