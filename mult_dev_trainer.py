import random


def get_multiplication():
    one = random.randint(2, 20)
    two = random.randint(2, 5)
    return one, two


def get_division():
    one, two = random.choice([
        [20, 2],
        [18, 2],
        [16, 2],
        [14, 2],
        [12, 2],
        [10, 2],
        [8, 2],
        [6, 2],
        [4, 2],
        [21, 3],
        [18, 3],
        [15, 3],
        [12, 3],
        [9, 3],
        [6, 3],
        [24, 4],
        [20, 4],
        [16, 4],
        [12, 4],
        [8, 4]
    ])
    return one, two


def get_task():
    sign = random.choice(['*', '/'])
    if sign == '*':
        one, two = get_multiplication()
        result = one * two
        return one, two, sign, result

    elif sign == '/':
        one, two = get_division()
        result = one / two
        return one, two, sign, result


def main():
    wrong = 0
    for i in range(40):
        one, two, sign, result = get_task()

        input(f'{one} {sign} {two} = ')
        if result == int(result):
            print('Верно')
        else:
            print('Неверно')
            wrong += 1

    print(f'Правильных ответов: {40 - wrong} из 40')


if __name__ == '__main__':
    main()
