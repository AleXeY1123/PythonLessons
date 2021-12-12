def func(*args):
    '''Возвращает сумму аргументов'''
    sum_args = 0
    for i in range(0, len(args)):
        sum_args += args[i]
    return sum_args

print(func(1,2,3,4,5,6.6))