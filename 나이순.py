n=int(input())

array=[]
for _ in range(n):

    
    a=input().split(' ')
    array.append((int(a[0]),a[1]))    
array= sorted(array, key=lambda x: x[0])   

for i in array:
    print(i[0], i[1])
