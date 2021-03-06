import numpy as np
import timeit
from time import time

a = int(input('Введите число строк: '))
b = int(input('Введите число столбцов: '))
m1 = np.random.randint(-50, 50, (a, b))
m2 = np.random.randint(-50, 50, (a, b))
print(m1, m2, sep='\n\n', end='\n\n\n')

print('Сумма: \n', m1 + m2, '\n\nПроизведение: \n', m1 * m2)

try:
    print('\n\nОпределитель первой матрицы: ', np.linalg.det(m1))
    print('Определитель второй матрицы: ', np.linalg.det(m2))
except:
    print('\n\nНевозможно вычислить определители')

try:
    print('\n\nОбратная матрица для первой:\n', np.linalg.inv(m1))
    print('\n\nОбратная матрица для второй:\n', np.linalg.inv(m2))
except:
    print('\n\nОбратные матрицы не существуют')


def save_matrix(matrix):
    try:
        with open('result.txt', 'w') as g:
            g.write(str(matrix))

    except Exception as error:
        print('\n', error)

    try:
        with open('matrix') as f:
            l = f.readlines()
            l1 = [list(map(int, l[i].split())) for i in range(len(l))]
            m = np.array(l1)
            print('\nОбратная матрица из файла:\n', np.linalg.inv(m))
    except Exception as err:
        print(err)


start = time()
np.linalg.inv(np.random.randint(-50, 50, (10, 10)))
print('\nВремя обращения матрицы 10х10: ', time() - start)

start = time()
np.linalg.inv(np.random.randint(-50, 50, (100, 100)))
print('\nВремя обращения матрицы 100х100: ', time() - start)

start = time()
np.linalg.inv(np.random.randint(-50, 50, (1000, 1000)))
print('\nВремя обращения матрицы 1000х1000: ', time() - start)

# start = time()
# np.linalg.inv(np.random.randint(-50, 50, (8728, 8728)))
# print('\nВремя обращения матрицы 8728х8728(макс): ', time() - start)

save_matrix(np.linalg.inv(m1))
