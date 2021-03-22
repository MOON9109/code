n=int(input())
a=0
b=1
c=0
if n==0:
    print(a)
elif n==1:
    print(b)

else:
    while(n>=1):
        c=b
        b=a+b
        a=c
        

        n= n-1

        if n==1:
            print(b)
            
