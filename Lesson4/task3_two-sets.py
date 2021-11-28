import random
set1 = {random.randint(0, 20)}
set2 = {random.randint(0, 20)}

for i in range(0, 10):
    set1.add(random.randint(0, 20))
    set2.add(random.randint(0, 20))

print(f'Первый набор: {set1}')
print(f'Второй набор: {set2}')

print(f'Элементы, входящие одновременно в оба множества: {set1.intersection(set2)}')
print(f'Элементы, которые входят только в первое множество, но не входят во второе: {set1.difference(set2)}')
print(f'Элементы, которые входят только в второе множество, но не входят в первое: {set2.difference(set1)}')
print(f'Элементы, входящие в первое или второе, но не в оба сразу: {set1.symmetric_difference(set2)}')