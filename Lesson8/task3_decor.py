import random
import datetime
import time

def decor(func):
    def wrapper(a, b):
        time_begining = datetime.datetime.now() 
        out = func(a, b)
        time.sleep(2)
        time_end = datetime.datetime.now()
        running_time = time_end - time_begining
        str_log = ('Time beginning: ' + str(time_begining) + '\n'
                    + 'Result:' + str(out) + '\n' 
                    + 'Time end: ' + str(time_end) + '\n' 
                    + 'Running time: ' + str(running_time))
        with open('Lesson8/task3_log.txt','w') as f:
            f.write(str_log)
        return out
    return wrapper

@decor
def sort_bubble(quantity, range_num):
    '''Сортировка методом пузрька
    quantity - количество значений
    range_num - максимальное значение
    возвращает отсортированный список
    '''
    l = []
    for i in range(0, quantity):
        l.append(random.randint(0, range_num))
        
    for i in range(0, len(l)-1):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


print(sort_bubble(10,1586))
