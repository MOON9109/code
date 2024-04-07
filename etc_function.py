#Advanced lambda, Reduce, Map, Filter
#더 빠른 연산으로 추가 할 수 있다.

#lambda 장점: 힙 영역 사용 즉시 소멸
#일반 함수 :재사용성 위해 메모리 저장
#시쿼늣형 전처리에 Reduce, Map, filter 주로 사용

#Ex1
curl= lambda a,b,c:a*b+c
print('Ex1',curl(10,15,20))
#Ex2
digits1=[x*10 for x in range(1,11)]
print('Ex2>',digits1)

result=list(map(lambda i:i**2,digits1))
print(result)

def also_square(nums):
    def double(x):
        return x**2
    return map(double,nums)

print('Ex2>',list(also_square(digits1)))

#Ex3
digits2=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x:x%2==0,digits2))
print('Ex3>',result)

def also_evens(nums):
    def is_even(x):
        return x%2==0
    return filter(is_even,nums)

print('Ex3>',list(also_evens(digits2)))

#Ex4
from functools import reduce
digits3=[x for x in range(1,101)]
result=reduce(lambda x,y:x+y,digits3)
print('Ex4>',result)


def also_add(nums):
    def add_plus(x,y):
        return x+y
    return reduce(add_plus,nums)

print('Ex4>',also_add(digits3))