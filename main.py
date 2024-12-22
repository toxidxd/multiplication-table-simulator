import random

mult_table = list()
task_table = list()

for x in range(2, 10):
    for y in range (2, 10):
        # print(f'{x} * {y} = ')
        mult_table.append(f'{x} * {y} = ')

for _ in range(32):
    # print(tab[random.randint(0, len(tab) - 1)])
    task_table.append(mult_table[random.randint(0, len(mult_table) - 1)])

with open('task.txt', 'w', encoding='utf-8') as f:
    for line in task_table:
        f.write(line + '\n')

print('File wrote.')
