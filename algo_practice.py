#Bubble Sort
import random
import time

startTime = time.time()

l = range(100000)

random.shuffle(l)

for i in range(len(l)):
        for j in range (len(l)-1):
            if l[j] > l[i]:
                l[i],l[j] = l[j],l[i]
print l

elapsedTime = time.time() - startTime
print elapsedTime
