import random


def gen_mult_table():
    result = list()
    for x in range(2, 10):
        for y in range(2, 10):
            result.append([x, y])

    return result


def gen_task_table(table):
    result = list()
    for _ in range(32):
        result.append(table[random.randint(0, len(table) - 1)])

    return result


mult_table = gen_mult_table()
task_table = gen_task_table(mult_table)

print('Добро пожаловать в тренажер таблицы умножения!')

for task in task_table:
    while True:
        try:
            answer = int(input(f'{task[0]} * {task[1]} = '))
            if answer == task[0] * task[1]:
                print(f'Правильно!')
                break
            else:
                print('Неправильно!')

        except ValueError as exc:
            print('Ответ должен быть числом!')
