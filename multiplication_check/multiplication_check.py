import os
import platform
import time
from datetime import datetime
import secrets

SEPARATOR_LEN = 70
SEPARATOR = "-"
GAME_NAME = 'Перевірка таблиці множення'
GAME_VER = 'v0.4'


def clear_screen(timeout=0):
    time.sleep(timeout)
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def print_head(length=None, pr2file=False):
    title = GAME_NAME + ' ' + GAME_VER
    clear_screen()
    if not length:
        length = SEPARATOR_LEN
    title_text = f"{title:{SEPARATOR}^{length}}\n"
    if pr2file:
        return title_text
    else:
        print(title_text)
    


def print_sep(length=None, pr2file=False):
    if not length:
        length = SEPARATOR_LEN
    text = SEPARATOR * length
    if pr2file:
        return text
    else:
        print(text)
    


def pause(length=None):
    if not length:
        length = SEPARATOR_LEN
    print_sep(length)
    input('Для продовження натисніть "Enter"')


def ask_multipliers():
    while True:
        try:
            print_head()
            print_sep()
            inp_multipliers = list(map(int,
                                       input('Вкажить на які множники треба перевірити таблицю множення\n'
                                             '(можна ввести декілька множників, наприклад "2 3"): ').split()))
            if not inp_multipliers:
                print('Ви не вказали жодного множника. Спробуйте ще раз.')
                clear_screen(2)
            else:
                return inp_multipliers
        except ValueError:
            print('Ви ввели не цифри! Спробуйте ще раз.')
            clear_screen(2)


def ask_qty():
    while True:
        try:
            print_head()
            print_sep()
            inp_qty = int(input('Вкажіть кількість прикладів для перевірки (наприклад "10"): '))
            return inp_qty
        except ValueError:
            print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
            clear_screen(2)


def ask_mistakes():
    while True:
        try:
            print_head()
            print_sep()
            inp_mistakes = int(input('Вкажіть кількість дозволених помилок (наприклад "2"): '))
            return inp_mistakes
        except ValueError:
            print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
            clear_screen(2)


def ask_quit():
    while True:
        print_head()
        print_sep()
        repeat = input("Повторити? ТАК - 1 / НІ - 0: ")
        if repeat == '0' or repeat == '1':
            clear_screen(0.5)
            return repeat
        else:
            print('Ви нічого не вказали, або вказали невірне значення. Спробуйте ще раз.')
            clear_screen(2)


def print_message_1(in_multipliers, in_qty, in_mistakes, pr2file=False):
    issue = ", ".join(list(map(str, in_multipliers)))
    message = f'Перевірка знань таблиці множення на {issue}.\nВсього {in_qty} прикладів.\nДозволено {in_mistakes} помилки.'
    if pr2file:
        return message
    else:
        print_head()
        print_sep()
        print(message)
        print_sep()
        print('Щоб завершити тестування достроково - введіть "0".')
    


def run_checking(in_multipliers, in_qty, in_mistakes):
    user_mistakes = 0
    numbers = []
    multipliers_work = []
    stop_check = False
    min_time = None
    max_time = 0
    result_logging = []

    for number in range(in_qty):
        if not multipliers_work:
            multipliers_work = list(in_multipliers)
        if not numbers:
            numbers = [2, 3, 4, 5, 6, 7, 8, 9]
        result_logging.append([])
        a = secrets.choice(multipliers_work)
        b = secrets.choice(numbers)
        statement = f'{number + 1:>3}) {str(a) + " x " + str(b):>6} = '

        while True:
            try:
                print(statement, end='')
                start_time = time.time()
                c = int(input())
                end_time = time.time()
                result_logging[-1].append(f'{statement+str(c):<20}')
                execution_time = round(end_time - start_time, 1)
                result_logging[-1].append(f"{str(execution_time) + ' сек':>10}")
                if execution_time > max_time:
                    max_time = execution_time
                if not min_time or execution_time < min_time:
                    min_time = execution_time
                print(f'\t\t\t\t\t\t({execution_time} сек)')
                break
            except ValueError:
                print_sep()
                print('Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.')
                print_sep()
                time.sleep(3)

        if c == 0:
            stop_check = True
            break
        elif c != a * b:
            user_mistakes += 1
            print_sep()
            message_2 = f'Помилка {user_mistakes} з {in_mistakes} дозволенних! {a} x {b} = {a * b}'
            result_logging[-1].append(message_2)
            print(message_2)
            print_sep()
            time.sleep(3)
        multipliers_work.remove(a)
        numbers.remove(b)

        if user_mistakes > in_mistakes:
            break

    if stop_check:
        print_sep()
        message_3 = 'Тестування перервано достроково.'
        print(message_3)
    elif user_mistakes == 0:
        print_sep()
        message_3 = f"Вітаємо! У Вас нема помилок! Ви відмінник!\n" \
                    f"Найшвидша відповідь - {min_time} сек, а найдовша відповідь - {max_time} сек."
        print(message_3)
    elif user_mistakes <= in_mistakes:
        print_sep()
        message_3 = f'Ви допустили {user_mistakes} помилок. Але Ви не програли. Вітаємо!\n' \
                    f'Найшвидша відповідь - {min_time} сек, а найдовша відповідь - {max_time} сек.'
        print(message_3)
    else:
        message_3 = f"Ви програли, бо допустили {user_mistakes} помилок. А це більше, ніж дозволено."
        print(message_3)

    return {"logging": result_logging, "message": message_3}


def get_current_time(*args):
    cur_date = datetime.now().date()
    cur_time = datetime.now().time()
    if 'date' in args and 'time' not in args:
        return str(cur_date)
    elif 'time' in args and 'date' not in args:
        return f"{str(cur_time.hour):0>2}:{str(cur_time.minute):0>2}"
    elif 'date' in args and 'time' in args:
        return f"{str(cur_date)} {str(cur_time.hour):0>2}:{str(cur_time.minute):0>2}"
    else:
        return str(cur_date) + "_" + f"{str(cur_time.hour):0>2}" + f"{str(cur_time.minute):0>2}"


def get_file_name():
    current_path = os.getcwd()
    folder_path = os.path.join(current_path, 'Results')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return os.path.join(folder_path, ("Result_" + get_current_time() + ".txt"))


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
        logfile = open(get_file_name(), "w")
        print(print_head(pr2file=True), file=logfile)
        print(f"Дата: {get_current_time('date')}\nЧас: {get_current_time('time')}", file=logfile)
        print('\n' + print_sep(pr2file=True) + '\n', file=logfile)

        multipliers = ask_multipliers()
        clear_screen(0.5)

        qty = ask_qty()
        clear_screen(0.5)

        mistakes = ask_mistakes()
        clear_screen(0.5)

        print_message_1(multipliers, qty, mistakes)
        pause()
        print_message_1(multipliers, qty, mistakes)
        print_sep()
        print()
        
        print(print_message_1(multipliers, qty, mistakes, pr2file=True), file=logfile)
        print('\n' + print_sep(pr2file=True) + '\n', file=logfile)

        result = run_checking(multipliers, qty, mistakes)

        for row in result['logging']:
            print(' | '.join(row), file=logfile)
        print('\n' + print_sep(pr2file=True) + '\n', file=logfile)
        print(result["message"], file=logfile)
        print('\n' + print_sep(pr2file=True), file=logfile)
        logfile.close()

        pause()
        clear_screen()

        if ask_quit() == '0':
            break

    goodbye()


if __name__ == "__main__":
    main()
