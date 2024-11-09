from collections import namedtuple

def calc(x, y):
    """두수를 입력받아 합, 곱, 나눈값을 반환한다 """
    return namedtuple(typename='return_calc', field_names=['sum', 'multiplication', 'division'])(x + y, x * y, x / y)

rr = calc(3, 2)
print('곱셈결과:', rr.multiplication) # 곱셈한 결과를 출력한다

dd = rr._asdict() # OrderedDict형으로 변환하여 사용할 수도 있다
print('곱셈결과:', dd['multiplication']) # 곱셈한 결과를 출력한다
