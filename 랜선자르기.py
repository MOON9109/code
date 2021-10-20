n,m= map(int, input().split(' '))
line=[]
num2=0
for _ in range(n):
    num= int(input())
    if num2<=num:
        num2=num
   
    line.append(num)

st=1
end=num2


result=0
while(st<=end):
    
    count=0
    mid=((end+st)//2)
    
    for x in range(n):
        count=count+ (line[x]//mid)
    if count<m:
        end=mid-1

    if count>m:
        st=mid+1
    if count==m:
        st=mid+1
       
        
print(end)
