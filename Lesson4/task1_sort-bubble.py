from operator import le
import random

l = []
for i in range(0, 50):
    l.append(random.randint(0, 1000))
    
for i in range(0, len(l)-1):
    for j in range(0, len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)