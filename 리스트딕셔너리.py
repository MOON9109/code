#리스트 활용방법
#리스트 선언
a=[]
a=list()

a=[1,2,3]
print(a)

a.append(4)
print(a)

a.insert(3,5) #인덱스 3에 5추가

print()
#제거 방법
del a[1] #인덱스 1위치 값 제거

print(a)

a.pop(3)
print()
print(a)

#딕셔너리

a=dict()

a={}

a={'key1':'value1','key2':'value2'}

print(a)

a['key3']='value3'
print(a)
print(a['key1'])

#키 , 값 꺼내기

for k,v in a.items():
    print(k,v)
