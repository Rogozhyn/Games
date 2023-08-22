import os
import platform
import time
from datetime import datetime
import secrets
import threading

SEPARATOR_LEN = 70
SEPARATOR = "-"
GAME_NAME = {'ua': 'Перевірка таблиці множення',
             'en': 'Checking the multiplication table'}
GAME_VER = 'v0.6'
LANGUAGE = 'ua'

messages = {
    'ask_multipliers':
        {'ua': ('Вкажить на які множники треба перевірити таблицю множення\n'
                '(можна ввести декілька множників, наприклад "2 3"): ',
                'Ви не вказали жодного множника. Спробуйте ще раз.',
                'Ви ввели не цифри! Спробуйте ще раз.'),
         'en': ('Specify which factors to check the multiplication table for\n'
                '(you can enter several multipliers, for example "2 3"): ',
                'You have not specified any multiplier. Try again.',
                'You entered not the numbers! Try again.')
         },
    'ask_qty':
        {'ua': 'Вкажіть кількість прикладів для перевірки (наприклад "10"): ',
         'en': 'Specify the number of examples to check (for example "10"): '
         },
    'ask_mistakes':
        {'ua': 'Вкажіть кількість дозволених помилок (наприклад "2"): ',
         'en': 'Specify the number of mistakes allowed (for example "2"): '
         },
    'ask_quit':
        {'question':
             {'ua': 'Повторити?', 'en': 'Repeat?'
              },
         'answers':
             {'1': ({'ua': 'ТАК', 'en': 'YES'}, '1'),
              '0': ({'ua': 'НІ', 'en': 'NO'}, '0')
              }
         },
    'wrong_int':
        {'ua': 'Ви нічого не ввели, або ввели не цифри! Спробуйте ще раз.',
         'en': "You didn't enter anything, or you entered the wrong numbers! Try again."
         },
    'wrong_choice':
        {'ua': 'Ви нічого не вказали, або вказали невірне значення. Спробуйте ще раз.',
         'en': 'You did not specify anything, or you specified an incorrect value. Try again.'},
    'pause':
        {'ua': 'Для продовження натисніть "Enter"',
         'en': 'Press "Enter" to continue'
         },
    'message_1':
        {'ua': ("f'Перевірка знань таблиці множення на {issue}.'",
                "f'Всього {in_qty} прикладів.'",
                "f'Дозволено {in_mistakes} помилки.'",
                'Щоб завершити тестування достроково - введіть "0".'),
         'en': ("f'Checking knowledge of the multiplication table by {issue}.'",
                "f'Only {in_qty} examples.'",
                "f'{in_mistakes} mistakes are allowed.'",
                'To interrupt testing early - enter "0".')
         },
    'message_2':
        {'ua': "f'Помилка {user_mistakes} з {in_mistakes} дозволених! {a} x {b} = {a * b}'",
         'en': "f'Mistake {user_mistakes} of {in_mistakes} allowed! {a} x {b} = {a * b}'"
         },
    'message_3':
        {'ua': ('Тестування перервано достроково.',
                'Вітаємо! У Вас немає помилок! Ви відмінник!',
                'f"Ви допустили {in_user_mistakes} помилок. Але Ви не програли. Вітаємо!"',
                'f"Ви програли, бо допустили {in_user_mistakes} помилок. А це більше, ніж дозволено."',
                'f"Найшвидша відповідь - {in_min_time} сек, а найдовша відповідь - {in_max_time} сек."'),
         'en': ('Testing was interrupted prematurely.',
                'Congratulations! You have no mistakes! You are excellent!',
                'f"You made {in_user_mistakes} mistake(s). But you did not lose. Congratulations!"',
                'f"You lost because you made {in_user_mistakes} mistake(s). And this is more than allowed."',
                'f"The fastest response is {in_min_time} sec, and the longest response is {in_max_time} sec."')
         },
    'goodbye':
        {'ua': 'До зустрічі!',
         'en': 'Goodbye!'
         },
    'date':
        {'ua': 'Дата',
         'en': 'Date'
         },
    'time':
        {'ua': 'Час',
         'en': 'Time'
         },
    'sec':
        {'ua': 'сек',
         'en': 'sec'
         },
}


def clear_screen(timeout=0):
    time.sleep(timeout)
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


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
    print(messages['goodbye'][LANGUAGE])
    time.sleep(0.5)
    print("...")
    time.sleep(0.4)
    print("..")
    time.sleep(0.3)
    print(".")
    time.sleep(0.2)
    exit()


def print_head(length=None, pr2file=False):
    title = GAME_NAME[LANGUAGE] + ' ' + GAME_VER
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


def print_message_1(in_multipliers, in_qty, in_mistakes, pr2file=False):
    issue = ", ".join(list(map(str, in_multipliers)))
    message = messages['message_1'][LANGUAGE]
    composed_message = f'{eval(message[0])}\n{eval(message[1])}\n{eval(message[2])}'
    if pr2file:
        return composed_message
    else:
        print_head()
        print_sep()
        print(composed_message)
        print_sep()
        print(message[3])


def print_message_3(in_stop_check, in_user_mistakes, in_in_mistakes, in_min_time, in_max_time):
    message_3_combined = messages['message_3'][LANGUAGE]
    if in_stop_check:
        clear_screen()
        print_sep()
        message = message_3_combined[0]
        print(message)
    elif in_user_mistakes == 0:
        print_sep()
        message = message_3_combined[1] + '\n' + eval(message_3_combined[4])
        print(message)
    elif in_user_mistakes <= in_in_mistakes:
        print_sep()
        message = eval(message_3_combined[2]) + '\n' + eval(message_3_combined[4])
        print(message)
    else:
        message = eval(message_3_combined[3])
        print(message)
    return message


def pause(length=None):
    if not length:
        length = SEPARATOR_LEN
    print_sep(length)
    input(messages['pause'][LANGUAGE])


def ask_language():
    answers = {'1': ('українська', 'ua'), '2': ('english', 'en')}
    while True:
        clear_screen()
        print('Виберіть мову / Choose a language:\n')
        for key in answers.keys():
            print(f'{key:>2}: {answers.get(key)[0]}')
        choice = input("\n>>: ")
        time.sleep(0.5)
        if choice in answers.keys():
            clear_screen()
            return answers.get(choice)[-1]
        else:
            clear_screen()
            print("Ви вказали не існуючий варіант. Спробуйте ще раз.\n"
                  "You specified an option that does not exist. Try again.")
            time.sleep(4)


def ask_multipliers():
    message = messages['ask_multipliers'][LANGUAGE]
    while True:
        try:
            print_head()
            print_sep()
            print(message[0], end='')
            inp_multipliers = list(map(int, input().split()))
            if not inp_multipliers:
                print(message[1])
                clear_screen(2)
            else:
                return inp_multipliers
        except ValueError:
            print(message[2])
            clear_screen(2)


def ask_int(message):
    while True:
        try:
            print_head()
            print_sep()
            print(message[LANGUAGE], end='')
            inp_qty = int(input())
            return inp_qty
        except ValueError:
            print(messages['wrong_int'][LANGUAGE])
            clear_screen(2)


def ask_choice(message):
    question = message['question']
    answers = message['answers']
    while True:
        print_head()
        print_sep()
        print(question[LANGUAGE], end='\n\n')
        for key in answers.keys():
            print(f'{key:>2}: {answers.get(key)[0][LANGUAGE]}')
        choice = input("\n>>: ")
        time.sleep(0.5)
        if choice in answers.keys():
            clear_screen()
            return answers.get(choice)[-1]
        else:
            clear_screen()
            print(messages['wrong_choice'][LANGUAGE])
            time.sleep(2)


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
                result_logging[-1].append(f'{statement + str(c):<20}')
                execution_time = round(end_time - start_time, 1)
                execution_time_str = str(execution_time) + ' ' + messages['sec'][LANGUAGE]

                result_logging[-1].append(f"{execution_time_str:>10}")
                if execution_time > max_time:
                    max_time = execution_time
                if not min_time or execution_time < min_time:
                    min_time = execution_time
                print(f"\t\t\t\t\t\t{execution_time_str}")
                break
            except ValueError:
                print_sep()
                print(messages['wrong_int'][LANGUAGE])
                print_sep()
                time.sleep(3)

        if c == 0:
            stop_check = True
            break
        elif c != a * b:
            user_mistakes += 1
            print_sep()
            message_2 = eval(messages["message_2"][LANGUAGE])
            result_logging[-1].append(message_2)
            print(message_2)
            print_sep()
            time.sleep(3)

        multipliers_work.remove(a)
        numbers.remove(b)
        clear_screen(0.5)

        if user_mistakes > in_mistakes:
            break

    message_3 = print_message_3(stop_check, user_mistakes, in_mistakes, min_time, max_time)
    return {"logging": result_logging, "message": message_3}


def main():
    global LANGUAGE
    LANGUAGE = ask_language()
    print_head()
    clear_screen(1)

    while True:
        logfile = open(get_file_name(), "w")
        print(print_head(pr2file=True), file=logfile)
        print(f"{messages['date'][LANGUAGE]}: {get_current_time('date')}\n"
              f"{messages['time'][LANGUAGE]}: {get_current_time('time')}", file=logfile)
        print('\n' + print_sep(pr2file=True) + '\n', file=logfile)

        multipliers = ask_multipliers()
        clear_screen(0.5)

        qty = ask_int(messages['ask_qty'])
        clear_screen(0.5)

        mistakes = ask_int(messages['ask_mistakes'])
        clear_screen(0.5)

        print_message_1(multipliers, qty, mistakes)
        pause()
        clear_screen()

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

        if ask_choice(messages['ask_quit']) == '0':
            break

    goodbye()


if __name__ == "__main__":
    main()
