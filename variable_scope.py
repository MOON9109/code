#closure
def outer():
    e=70
    def inner():
        nonlocal e
        e+=10
        print('Ex5>',e)
    return inner

in_test =outer() #closure


in_test()
in_test()
in_test()


def func(var):
    x=10
    def printer():
        print('Ex6>','printer Func Inner')
    print('Func Inner', locals())
#locals :해당 영역에 있는 것들을 dictionary로 출력해줌
func('Hi')


#globals
print('Ex7',globals())
test_variable=100
print('Ex7',globals())


#Ex8 (지역 -> 전역 변수 생성)
for i in range(1,10):
    for k in range(1,10):
        globals()['plus_{}_{}'.format(i,k)]=i+k
print(globals())


print('Ex8>', plus_5_5)
print('Ex8>', plus_9_9)



