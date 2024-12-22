import random

print("Таблица умножения для сыночки")

tab = list()
cur_tab = list()

for x in range(2, 10):
    for y in range (2, 10):
        # print(f'{x} * {y} = ')
        tab.append(f'{x} * {y} = {x * y}')

for _ in range(32):
    # print(tab[random.randint(0, len(tab) - 1)])
    cur_tab.append(tab[random.randint(0, len(tab) - 1)])

with open('task.txt', 'w', encoding='utf-8') as f:
    for line in cur_tab:
        f.write(line + '\n')

