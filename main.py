import logging
import random
import time

# import sys


logging.basicConfig(level='INFO')
logger = logging.getLogger(name='result_log')
logger.propagate = False

# custom_handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter(
    fmt="%(asctime)s | %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
)
# custom_handler.setFormatter(formatter)

file_handler = logging.FileHandler(
    filename='Результаты тренажера по умножению.txt', encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# logger.addHandler(custom_handler)


def gen_mult_table() -> list[list[int]]:
    result = list()
    for x in range(3, 20):
        for y in range(3, 20):
            result.append([x, y, x * y])
    return result


def gen_task_table(count: int) -> list[list[int]]:
    mul_table = gen_mult_table()
    indexes = list(range(len(mul_table)))
    random.shuffle(indexes)
    indexes = indexes[:count]
    return [mul_table[i_index] for i_index in indexes]


def mix_tasks(tasks_count):
    logger.info(f'{mix_tasks.__name__} | Начало задания на смешанные примеры')
    errors_count = 0
    task_table = gen_task_table(tasks_count)

    for num, task in enumerate(task_table):
        while True:
            try:
                mult_or_div = random.randint(0, 1)

                if mult_or_div == 0:
                    answer = int(input(f'{num + 1}) {task[0]} * {task[1]} = '))
                    if answer == task[2]:
                        print(f'Правильно!')
                        break
                    else:
                        errors_count += 1
                        print('Неправильно!')

                else:
                    answer = int(input(f'{num + 1}) {task[2]} / {task[0]} = '))
                    if answer == task[2] / task[0]:
                        print(f'Правильно!')
                        break
                    else:
                        errors_count += 1
                        print('Неправильно!')

            except ValueError:
                print('Ответ должен быть числом!')

    if errors_count != 0:
        print(f'Количество ошибок: {errors_count}')
        logger.info(
            f'{mix_tasks.__name__} | Количество ошибок: {errors_count}')
        additional_tasks(choice=3, errors_count=errors_count)


def multiplication(tasks_count):
    logger.info(f'{multiplication.__name__} | Начало задания на умножение')
    errors_count = 0
    task_table = gen_task_table(tasks_count)

    for num, task in enumerate(task_table):
        while True:
            try:
                answer = int(input(f'{num + 1}) {task[0]} * {task[1]} = '))
                if answer == task[2]:
                    print(f'Правильно!')
                    break
                else:
                    errors_count += 1
                    print('Неправильно!')

            except ValueError:
                print('Ответ должен быть числом!')

    if errors_count != 0:
        print(f'Количество ошибок: {errors_count}')
        logger.info(
            f'{multiplication.__name__} | Количество ошибок: {errors_count}')
        additional_tasks(choice=1, errors_count=errors_count)


def division(tasks_count):
    logger.info(f'{division.__name__} | Начало задания на деление')

    errors_count = 0
    task_table = gen_task_table(tasks_count)

    for num, task in enumerate(task_table):
        while True:
            try:
                answer = int(input(f'{num + 1}) {task[2]} / {task[0]} = '))
                if answer == task[2] / task[0]:
                    print(f'Правильно!')
                    break
                else:
                    errors_count += 1
                    print('Неправильно!')

            except ValueError:
                print('Ответ должен быть числом!')

    if errors_count != 0:
        print(f'Количество ошибок: {errors_count}')
        logger.info(f'{division.__name__} | Количество ошибок: {errors_count}')
        additional_tasks(choice=2, errors_count=errors_count)


def additional_tasks(choice, errors_count):
    print(
        f'За ошибки в предыдущих заданиях ты будешь решать дополнительные примеры. ({errors_count * 2})')
    logger.info(
        f'{additional_tasks.__name__} | Дополнительные примеры: {errors_count * 2}')
    start_task(my_choice=choice, tasks_count=errors_count * 2)


def start_task(my_choice=None, tasks_count=None):
    if my_choice is None:
        print('Выберите задание \n\t1 - умножение\n\t2 - деление\n\t3 - смешанные задания')
        my_choice = int(input('Ваш выбор: '))
        logger.info(f'{start_task.__name__} | Выбрано задание: {my_choice}')
    if tasks_count is None:
        tasks_count = int(input('Количество примеров: '))
        logger.info(
            f'{start_task.__name__} | Количество примеров: {tasks_count}')

    if my_choice == 1:
        multiplication(tasks_count)
    elif my_choice == 2:
        division(tasks_count)
    elif my_choice == 3:
        mix_tasks(tasks_count)
    else:
        print('Неверный ввод!')


def main():
    print('Добро пожаловать в тренажер таблицы умножения и деления!')
    start = time.time()

    start_task()

    end = time.time()
    elapsed_time = (end - start) // 60

    print(f'Время выполнения: {elapsed_time} минут')

    input('Нажмите Enter для продолжения...')


if __name__ == '__main__':
    main()
