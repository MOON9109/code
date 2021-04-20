a=input()
b=input()
count=0
x=0
while(x<len(a)):    
    if a[x:x+len(b)]== b:
        x=x+len(b)
        count =count +1
        continue
    x=x+1
print(count)
