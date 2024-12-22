import random
import time
from operator import index


def gen_mult_table() -> list[list[int]]:
    result = list()
    for x in range(2, 10):
        for y in range(2, 10):
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


def main():
    print('Добро пожаловать в тренажер таблицы умножения!')

    mult_table = gen_mult_table()
    errors_count = 0

    tasks_count = int(input('Количество примеров: '))
    task_table = gen_task_table(mult_table, tasks_count)

    start = time.time()
    for task in task_table:
        while True:
            try:
                answer = int(input(f'{task[0]} * {task[1]} = '))
                if answer == task[0] * task[1]:
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


if __name__ == '__main__':
    main()
