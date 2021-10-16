import itertools

n=int(input())
score=[]

for _ in range(n):
    num= list(map(int, input().split(' ')))
    score.append(num)
    
#print(score)
#a=[1,2,3,4]
a=[x for x in range(n)]
b=int(n/2)
com =list(itertools.combinations(a,b))
n=len(com)
c=int(n/2)
com2=com[:c]

result=999999

for m in com2:
    team1=0
    team2=0
    
    m3=list(itertools.permutations(m,2))
    
    
    for k in m3:
        x1,y1=k
        team1=team1+score[x1][y1]
        
    m2=set(m)
    a2=set(a)
    m4=list(a2.difference(m2))
    
    m5=list(itertools.permutations(m4,2))
    
    
    for k2 in m5:
        x2,y2=k2
        
        
        team2=team2+score[x2][y2]

    if result>abs(team1-team2):
        result=abs(team1-team2)

print(result)
