def factorial(n):
    ''' Factorial Function -> n :int '''
    if n==1:
        return 1
    return n* factorial(n-1)

class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial),type(A))

print(set(sorted(dir(factorial)))-set(sorted(dir(A))))

print(factorial.__name__)
print(factorial.__code__)

#변수 할당

var_func =factorial
print(var_func)
print(var_func(10))
print(list(map(var_func,range(1,11))))

#함수 인수 전달 및 함수로 결과 반환
#map , filter, reduce

print(list(map(var_func, filter(lambda x:x%2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i%2])

print()
print()

from functools import reduce
from operator import add

print(reduce(add,range(1,11)))

# 익명함수 (lambda)
print(reduce(lambda x,t:x+t ,range(1,11)))

#callable 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print( callable(str))
print(callable(str),callable(list),callable(var_func),callable(factorial),callable(3.14))

#partial 사용법 : 인수 고정 -> 콜백 함수 사용

from operator import  mul
from functools import partial

five =partial(mul,5)

print(five(10))
six=partial(five,6)

print(five(10))
print(six())
