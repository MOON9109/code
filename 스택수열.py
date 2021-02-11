n=int(input())
count=1
result=[]
stack=[]
for x in range(n):
    data=int(input())

    while(count<=data):
        stack.append(count)
        result.append('+')
        count=count+1
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        result.append('NO')
        

if 'NO' in result:
    print('NO')
else:
    for x in result:
        print(x)
