n,m=map(int, input().split(' '))

num=list(map(int,input().split(' ')))


s=max(num)
e=sum(num)

while(s<=e):
    
    
    sumnum=0
    count=0
    mid=(s+e)//2
   
    
    for x in num:
        sumnum=sumnum+x
        if sumnum>mid:
            count=count+1
            sumnum=x
    if sumnum!=0:
        count=count+1
   
    if count>m:
        s=mid+1
    if count<=m:
        
        e=mid-1

       
        
print(s)
