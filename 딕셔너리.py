#딕셔너리

#사전 자료형은 키(key)와 값(Value)의 쌍을 데이터로 가지는 자료형입니다
# 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다

#사전 자료형은 키와 값의 쌍을 데이터로 가지며 원하는 "변경 불가능한 자료형"을 키로 사용 할 수 있습니다
#파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.

data =dict()
data['사과'] ='Apple'
data['바나나'] ='Banana'
data['코코넛'] ='Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")
    
#데이터의 조회가 리스트보다 빠르다


#딕셔너리형 관련 메서드
'''
사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원합니다.
키 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수를 이용합니다.
값 데이터만을 뽑아서 리스트로 이용할 때는 values()함수를 이용합니다.
'''


data =dict()
data['사과'] ='Apple'
data['바나나']= 'Banana'
data['코코넛']= 'Coconut'

key_list =data.keys()
#리스트로 사용하고자 한다면 keys를 통해 받은 후 list() 씌워줘야함

value_list =data.values()

print(key_list)
print(value_list)

for key in key_list:
    print(data[key])


