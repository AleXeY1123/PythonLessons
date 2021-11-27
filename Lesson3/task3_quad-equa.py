import math
print('Решение квадратного уравнения вида ax^2 + bx + c = 0')
a = float(input('Введите значение "a": '))
b = float(input('Введите значение "b": '))
c = float(input('Введите значение "c": '))

D = b ** 2 - 4 * a * c
print(f'Дискриминант = {D}')

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'есть два корня, x1 = {x1}, x2 = {x2}')
elif D == 0:
    x = -b / (2 * a)
    print(f'есть один корень = {x}')
else:
    print('корней нет')
