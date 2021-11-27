import math
import cmath

print('Решение квадратного уравнения вида ax^2 + bx + c = 0')
a = input('Введите значение "a": ')
b = input('Введите значение "b": ')
c = input('Введите значение "c": ')

if a.find('j') != -1:
    a = complex(a)
else:
    a = float(a)

if b.find('j') != -1:
    b = complex(b)
else:
    b = float(b)

if c.find('j') != -1:
    c = complex(c)
else:
    c = float(c)

D = b ** 2 - 4 * a * c
print(f'Дискриминант = {D}')

if str(type(D)) == "<class 'complex'>":
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f'есть два корня, x1 = {x1}, x2 = {x2}')
elif D < 0:
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f'есть два корня, x1 = {x1}, x2 = {x2}')
elif D==0:
    x = -b / (2 * a)
    print(f'есть один корень = {x}')
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'есть два корня, x1 = {x1}, x2 = {x2}')