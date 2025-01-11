import random
import time


def gen_mult_table() -> list[list[int]]:
    result = list()
    for x in range(2, 10):
        for y in range(2, 10):
            result.append([x, y, x * y])

    return result

def gen_div_table() -> list[list[int]]:
    result = list()
    for x in range(2, 10):
        for y in range(2, 10):
            if x > y:
             result.append([x, y])

    return result

def gen_task_table(table: list[list[int]], count: int) -> list[list[int]]:
    result = list()
    indexes = list(range(len(table)))
    random.shuffle(indexes)
    indexes = indexes[:count]
    for i_index in indexes:
        result.append(table[i_index])

    return result


def multiplication():
    print('Добро пожаловать в тренажер таблицы умножения!')
    tasks_count = int(input('Количество примеров: '))

    mult_table = gen_mult_table()
    errors_count = 0
    task_table = gen_task_table(mult_table, tasks_count)

    start = time.time()
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

            except ValueError as exc:
                print('Ответ должен быть числом!')

    end = time.time()
    elapsed_time = (end - start) // 60

    print(f'Молодец, ты справился!\nКоличество ошибок: {errors_count}')
    print(f'Время выполнения: {elapsed_time} минут')

    while True:
        pass


def division():
    print('Добро пожаловать в тренажер деления!')
    tasks_count = int(input('Количество примеров: '))

    div_table = gen_div_table()
    errors_count = 0
    task_table = gen_task_table(div_table, tasks_count)

    start = time.time()
    for num, task in enumerate(task_table):
        while True:
            try:
                answer = int(input(f'{num + 1}) {task[0]} / {task[1]} = '))
                if answer == task[0] / task[1]:
                    print(f'Правильно!')
                    break
                else:
                    errors_count += 1
                    print('Неправильно!')

            except ValueError as exc:
                print('Ответ должен быть числом!')

    end = time.time()
    elapsed_time = (end - start) // 60

    print(f'Молодец, ты справился!\nКоличество ошибок: {errors_count}')
    print(f'Время выполнения: {elapsed_time} минут')

    while True:
        pass


def main():
    print('Добро пожаловать в тренажер таблицы умножения и деления!')
    print('Выберите задание \n\t1 - умножение\n\t2 - деление')
    my_choice = int(input('Ваш выбор: '))
    if my_choice == 1:
        multiplication()
    elif my_choice == 2:
        division()
    else:
        print('Неверный ввод!')


if __name__ == '__main__':
    main()
