#피보나치 수열 (재귀적)

#한번 계산된 결과를 기록하기 위한 리스트 초기화
d=[0]*100
#피보나치 함수를 재귀 함수로 구현
def fibo(x):
    #종료 조건 (1혹은 2일 때 1을 반환)

    if x==1 or x==2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))
print(d)
