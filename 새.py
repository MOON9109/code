n=int(input())
count=0
sumnum=0
num=1
while(True):
    if n>=num:
        n=n-num
        num=num+1
        count =count+1
    if n==0:
        break

    if n<num:
        num=1

print(count)
    

    
    
