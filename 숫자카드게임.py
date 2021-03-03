n, m =map(int, input().split())

count =0
result =0
minnum =[]
while(count<n):

    data =list(map(int, input().split()))
    minvalue =min(data)
    result = max(result, minvalue)

    count=count+1    

print(result)
