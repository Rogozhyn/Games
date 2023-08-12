import os
import platform
import time
import secrets
from random import randint

SEPARATOR_LEN = 50
SEPARATOR = "-"
GAME_NAME = 'Перевірка таблиці множення'
GAME_VER = 'v0.1'


def clear_screen(timeout=0):
    time.sleep(timeout)
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def print_head():
    title = GAME_NAME + ' ' + GAME_VER
    clear_screen()
    print(f"{title:{SEPARATOR}^{SEPARATOR_LEN}}")


def print_sep():
    print(SEPARATOR * SEPARATOR_LEN)


def pause():
    print_sep()
    input('Для продовження натисніть "Enter"')


def goodbye():
    print("До зустрічі!")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    exit()


def main():
    print_head()
    clear_screen(3)

    while True:
        while True:
            try:
                multipliers = list(map(int,
                                       input('Вкажить на які множники треба перевірити таблицю множення: ').split()))
                if not multipliers:
                    print('Ви не вказали жодного множника. Спробуйте ще раз.')
                    clear_screen(2)
                else:
                    break
            except ValueError:
                print('Ви ввели не цифри! Спробуйте ще раз.')
                clear_screen(2)
        clear_screen(0.5)

        while True:
            try:
                qty = int(input('Вкажіть кількість прикладів для перевірки: '))
                break
            except ValueError:
                print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                clear_screen(2)
        clear_screen(0.5)

        while True:
            try:
                mistakes = int(input('Вкажіть кількість дозволених помилок: '))
                break
            except ValueError:
                print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                clear_screen(2)
        clear_screen(0.5)

        user_mistakes = 0
        numbers = []
        multipliers_work = []
        for number in range(qty):
            if not multipliers_work:
                multipliers_work = list(multipliers)
            if not numbers:
                numbers = [2, 3, 4, 5, 6, 7, 8, 9]
            a = secrets.choice(multipliers_work)
            b = secrets.choice(numbers)
            print(f'{number+1}) {a} x {b} = ', end='')
            c = int(input())
            if c != a*b:
                print(f'Помилка! {a} x {b} = {a*b}')
                user_mistakes += 1
            multipliers_work.remove(a)
            numbers.remove(b)
            if user_mistakes > mistakes:
                print_sep()
                print(f"Ви програли, бо допустили {user_mistakes} помилок. А це більше, ніж дозволено.")
                break

        if user_mistakes == 0:
            print_sep()
            print("Вітаємо! У Вас нема помилок! Ви відмінник!")
        elif user_mistakes <= mistakes:
            print_sep()
            print(f'Ви допустили {user_mistakes} помилок. Але Ви не програли. Вітаємо.')
        pause()
        clear_screen()

        while True:
            repeat = input("Повторити? ТАК - 1 / НІ - 0: ")
            if repeat == '0' or repeat == '1':
                clear_screen(0.5)
                break
            else:
                print('Ви нічого не вказали, або вказали не вірне значення. Спробуйте ще раз.')
                clear_screen(2)

        if repeat == '0':
            break

    goodbye()


if __name__ == "__main__":
    main()
