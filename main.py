import random
import time


def gen_mult_table() -> list[list[int]]:
    result = list()
    for x in range(3, 9):
        for y in range(3, 9):
            result.append([x, y, x * y])
    return result


def gen_task_table(table: list[list[int]], count: int) -> list[list[int]]:
    result = list()
    indexes = list(range(len(table)))
    random.shuffle(indexes)
    indexes = indexes[:count]
    for i_index in indexes:
        result.append(table[i_index])

    return result

def mix_tasks():
    tasks_count = int(input('Количество примеров: '))

    div_table = gen_mult_table()
    errors_count = 0
    task_table = gen_task_table(div_table, tasks_count)

    start = time.time()
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


            except ValueError as exc:
                print('Ответ должен быть числом!')

    end = time.time()
    elapsed_time = (end - start) // 60

    well_done(errors_count, elapsed_time)

    while True:
        pass


def multiplication():
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

    well_done(errors_count, elapsed_time)

    while True:
        pass


def division():
    tasks_count = int(input('Количество примеров: '))

    div_table = gen_mult_table()
    errors_count = 0
    task_table = gen_task_table(div_table, tasks_count)

    start = time.time()
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

            except ValueError as exc:
                print('Ответ должен быть числом!')

    end = time.time()
    elapsed_time = (end - start) // 60

    well_done(errors_count, elapsed_time)

    while True:
        pass


def well_done(errors, time):
    print(f'Молодец, ты справился!\nКоличество ошибок: {errors}')
    print(f'Время выполнения: {time} минут')


def main():
    print('Добро пожаловать в тренажер таблицы умножения и деления!')
    print('Выберите задание \n\t1 - умножение\n\t2 - деление\n\t3 - смешанные задания')
    my_choice = int(input('Ваш выбор: '))
    if my_choice == 1:
        multiplication()
    elif my_choice == 2:
        division()
    elif my_choice == 3:
        mix_tasks()
    else:
        print('Неверный ввод!')


if __name__ == '__main__':
    main()
