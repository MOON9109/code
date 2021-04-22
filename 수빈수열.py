n= int(input())


lst=list(map(int, input().split()))


x=0
while(x<n):
    if x==0:
        print(lst[0],end='')
        print(' ',end='')
        x=x+1
        if n==1:
            break

    print((x+1)*lst[x]-x*lst[x-1],end='')
    print(' ',end='')
    x=x+1
    
