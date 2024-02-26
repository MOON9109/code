# 클로저
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print('inner >>> {} /{}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))

print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)
print(avg_closure1.__closure__[0])

x = avg_closure1(50)
print(f'x:{x}')


# 방법 2
def closure_ex2():
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex2()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(45))
