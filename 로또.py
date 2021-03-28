from itertools import combinations

while True:
    s= list(map(int,input().split()))
  
    if s[0]==0:
        break
    del s[0]
   
    s = list(combinations(s,6))
  
    for x in s:
        for a in x:
            print(a, end=' ')
        print()
    print()
