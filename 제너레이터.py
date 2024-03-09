

# 병행성(concurrency): 힌 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행


#generator Ex1


def generator_ex1():
    print('start')
    yield  'A Point'
    print('continue')
    yield 'B Point'
    print('End')

temp =iter(generator_ex1())


# print(dir(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    # print('-'*20)
    # print(v)
    pass


#generator Ex2

temp1 =[x*3 for x in generator_ex1()]
temp2 =(x*3 for x in generator_ex1())
# print(temp1)
# print(temp2)


for i in temp2:
    print(i)

for i in temp1:
    print(i)


#Gemerator 중요 함수


import itertools
gen1 =itertools.count(1,2.5)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))


gen2=itertools.takewhile(lambda n: n<1000, itertools.count(1,2.5))

for v in gen2:
    pass
    # print(v)

#필터 반대

gen3 =itertools.filterfalse(lambda n:n<3, [1,2,3,4,5])

# for v in gen3:
#     print(v)
gen4=itertools.accumulate([x for x in range(1,101)])

# print(gen4)
#
# for v in gen4:
#     print(v)

gen5 = itertools.chain('ABCDE',range(1,11,2))
print(list(gen5))

gen6=itertools.chain(enumerate('ABCDE'))
print(list(gen6))

gen7=itertools.product('ABCDE')
print(list(gen7))

gen8=itertools.product('ABCDE',repeat=2)
print(list(gen8))

#그룹화
gen9=itertools.groupby('AAAABBCCCDDDEEE')

for chr, group in gen9:
    print(chr,':',list(group))
