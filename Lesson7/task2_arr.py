import numpy as np

arr = np.random.randint(20, size=(3, 3))
print('Исходная матрица')
print(arr)
arr_transpon = np.transpose(arr)
print('Транспонированная матрица')
print(arr_transpon)
