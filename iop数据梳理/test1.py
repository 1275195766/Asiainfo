import random

l=[]

for i in range(3):
    l.append(random.randint(160000,189990))
l.sort()
for j in l:
    print(j)

# for j in l:
#     print(sum(j)//5)