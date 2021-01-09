#리스트 관련 메서드

a=[1,4,3]

print(f"기본 리스트: {a}")

a.append(2)
print(f"삽입된 리스트:{a} ")

#오름차순
a.sort()
print(f"오름차순 정렬:{a}")

#내림차순 정렬
a.sort(reverse =True)
print(f"내림차순 정렬:{a}")

#enumerate
x=['John','George','Paul','Ringo']

for i in range(len(x)):
    print(f'x[{i}] ={x[i]}')

print()
print('---------------------------')
for i,name in enumerate(x):
    print(f'x[{i}]={name}')
print()
print('---------------------------')
#인덱스 1부터 사용


for i, name in enumerate(x,1):
    print(f'{i}번째 ={name}')


