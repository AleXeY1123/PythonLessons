import numpy as np
from random import randint
arr = np.random.randint(20, size=(3, 3))
print('Исходная матрица')
print(arr)
arr_transpon = np.transpose(arr)
print('Транспонированная матрица')
print(arr_transpon)