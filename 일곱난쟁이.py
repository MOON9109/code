m=[]
import random
for x in range(9):
    n=int(input())
    m.append(n)
from itertools import combinations
data=[0,1,2,3,4,5,6,7,8]
result=list(combinations(data,2))


for x in result:
    a,b=x
    sum1=0
    k=[]
    for c in range(9):
        if (c!=a and c!=b):
            sum1=sum1+m[c]
            k.append(m[c])
    if sum1==100:
        break
k.sort()
for x in k:
    print(x)


    
