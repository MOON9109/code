#Palindrome
#example
'''
입력:
A man, a plan a canal: Panama"
출력:
true
'''
def Palindrome(s:str):
    strs=[]
    for char in s:
# isalnum 영문자, 숫자 여부 판별하는 함수 이를 통해 문자만 추가한다.

        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
#pop에 0 인덱스 지정해주면 맨 앞에 있는 값 출력 가능 이를 통해 뒤 값과 일치는지
#확인
        if strs.pop(0) !=strs.pop():
            return False


    return True
s="A man, a plan a canal: Panama"


print(Palindrome(s))
s2="race a car"
print(Palindrome(s2))
                
