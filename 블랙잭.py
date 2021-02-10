import itertools
n, m=map(int, input().split())

k=list(map(int, input().split()))

index=list(range(n))


index2 = list(map(list, itertools.combinations(index,3)))

total=[]
for x in index2:
    sumnum = 0
    sumnum2=0
    for y in x:
        sumnum=sumnum +k[y]

    
    if sumnum<=m:
        total.append(sumnum)

print(max(total))
