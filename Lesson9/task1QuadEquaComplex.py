import math
import cmath

def quadratic_equation(a, b, c):
    '''Решение квадратного уравнения вида ax^2 + bx + c = 0'''
    result = []
    if str(type(a)) == "<class 'str'>" and str(type(b)) == "<class 'str'>" and str(type(c)) == "<class 'str'>":
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
    else:
        print('Параметры должны быть строковыми')
        return 

    D = b**2 - 4 * a * c
    result.append(D)

    if str(type(D)) == "<class 'complex'>":
        x1 = (-b + cmath.sqrt(D)) / (2*a)
        x2 = (-b - cmath.sqrt(D)) / (2*a)
        result.append(2)
        result.append(x1)
        result.append(x2)
    elif D < 0:
        x1 = (-b + cmath.sqrt(D)) / (2*a)
        x2 = (-b - cmath.sqrt(D)) / (2*a)
        result.append(2)
        result.append(x1)
        result.append(x2)
    elif D==0:
        x = -b / (2 * a)
        result.append(1)
        result.append(x)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        result.append(2)
        result.append(x1)
        result.append(x2)
    return result

print(quadratic_equation('5', '1-2j', '-17'))