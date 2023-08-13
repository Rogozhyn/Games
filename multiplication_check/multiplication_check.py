import os
import platform
import time
import secrets

SEPARATOR_LEN = 60
SEPARATOR = "-"
GAME_NAME = 'Перевірка таблиці множення'
GAME_VER = 'v0.2'


def clear_screen(timeout=0):
    time.sleep(timeout)
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def print_head(length=None):
    title = GAME_NAME + ' ' + GAME_VER
    clear_screen()
    if not length:
        length = SEPARATOR_LEN
    print(f"{title:{SEPARATOR}^{length}}")


def print_sep(length=None):
    if not length:
        length = SEPARATOR_LEN
    print(SEPARATOR * length)


def pause(length=None):
    if not length:
        length = SEPARATOR_LEN
    print_sep(length)
    input('Для продовження натисніть "Enter"')


def goodbye():
    print("До зустрічі!")
    time.sleep(0.5)
    print("...")
    time.sleep(0.4)
    print("..")
    time.sleep(0.3)
    print(".")
    time.sleep(0.2)
    exit()


def main():
    print_head()
    clear_screen(1)

    while True:
        while True:
            try:
                print_head()
                print_sep()
                multipliers = list(map(int,
                                       input('Вкажить на які множники треба перевірити таблицю множення\n'
                                             '(можна ввести декілька множників, наприклад "2 3"): ').split()))
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
                print_head()
                print_sep()
                qty = int(input('Вкажіть кількість прикладів для перевірки (наприклад "10"): '))
                break
            except ValueError:
                print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                clear_screen(2)
        clear_screen(0.5)

        while True:
            try:
                print_head()
                print_sep()
                mistakes = int(input('Вкажіть кількість дозволених помилок (наприклад "2"): '))
                break
            except ValueError:
                print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                clear_screen(2)
        clear_screen(0.5)

        print_head()
        print_sep()
        issue = ", ".join(list(map(str, multipliers)))
        print(f'Перевірка знань таблиці множення на {issue}.')
        print(f'Всього {qty} прикладів.')
        print(f'Дозволено {mistakes} помилки.')
        print('Щоб завершити тестування достроково - введіть "0".')
        print_sep()
        time.sleep(4)

        user_mistakes = 0
        numbers = []
        multipliers_work = []
        stop_check = False

        for number in range(qty):
            if not multipliers_work:
                multipliers_work = list(multipliers)
            if not numbers:
                numbers = [2, 3, 4, 5, 6, 7, 8, 9]
            a = secrets.choice(multipliers_work)
            b = secrets.choice(numbers)
            while True:
                try:
                    print(f'{number + 1}) {a} x {b} = ', end='')
                    start_time = time.time()
                    c = int(input())
                    end_time = time.time()
                    execution_time = end_time - start_time
                    print(f'\t\t\t\t\t\t({round(execution_time, 1)} сек)')
                    break
                except ValueError:
                    print_sep()
                    print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                    print_sep()
                    time.sleep(3)
            if c == 0:
                stop_check = True
                break
            elif c != a*b:
                user_mistakes += 1
                print_sep()
                print(f'Помилка {user_mistakes} з {mistakes} дозволенних! {a} x {b} = {a*b}')
                print_sep()
                time.sleep(3)
            multipliers_work.remove(a)
            numbers.remove(b)
            if user_mistakes > mistakes:
                print(f"Ви програли, бо допустили {user_mistakes} помилок. А це більше, ніж дозволено.")
                break

        if stop_check:
            print_sep()
            print('Тестування перервано достроково.')
        elif user_mistakes == 0:
            print_sep()
            print("Вітаємо! У Вас нема помилок! Ви відмінник!")
        elif user_mistakes <= mistakes:
            print_sep()
            print(f'Ви допустили {user_mistakes} помилок. Але Ви не програли. Вітаємо.')
        pause()
        clear_screen()

        while True:
            print_head()
            print_sep()
            repeat = input("Повторити? ТАК - 1 / НІ - 0: ")
            if repeat == '0' or repeat == '1':
                clear_screen(0.5)
                break
            else:
                print('Ви нічого не вказали, або вказали невірне значення. Спробуйте ще раз.')
                clear_screen(2)

        if repeat == '0':
            break

    goodbye()


if __name__ == "__main__":
    main()
