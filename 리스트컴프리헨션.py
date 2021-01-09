#리스트 컴프리헨션

array =[ i for i in range(10)]

print(array)

array2= [i for i in range(20) if i%2==1] #홀수 인 것만 리스트 저장

print(array2)


array3= [ i*i for i in range(1,10)] # 제곱 형태로 리스트 저장
print(array3)


#N*M 크기의 2차원 리스트 초기화
n=4
m=3
array =[[0]*m for _ in range(n)]
print(array)
