n=int(input())
array=[]
for _ in range(n):
    a=list(map(int, input().split(' ')))
    array.append((a[0],a[1]))

# key 설정 없이 
array =sorted(array)

                 
for i in array:
    print(i[0], i[1])
