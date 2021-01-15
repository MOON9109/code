#리스트 컴프리헨션

a=list(map(lambda x: x+10 ,[1,2,3]))
print(a)

b=[n*2 for n in range(1,10+1) if n%2==1]
print(b)

#제너레이터
#제너레이터를 이용하면 필요할 때 언제든 숫자를 만들어낼 수 있다.

def get_natural_number():
    n=0
    while True:
        n+=1
        yield n




#g= get_natural_number()
#제너레이터 값을 출력하려면 next()를 이용해 출력
#for _ in range(0,100):
#    print(next(g))


def generator():
    yield 1
    yield 'string'
    yield True

g= generator()
print(next(g))
print(next(g))
print(next(g))


#enumerate
a=[1,2,3,2,45,2,5]

print(enumerate(a))

print(list(enumerate(a)))

#인덱스와 값 출력

for i,v in enumerate(a):
    print(i, v)

#join
a=['A','B','C']
print(' '.join(a))




    
