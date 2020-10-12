import random

l=[]

for i in range(10):
    l.append([random.randint(12000,16540) for i in range(5)])
print(l)
for j in l:
    print(sum(j)//5)