# 테스트 대상 기능
파일 이름
# test_*.py 또는 *_test.py 형식으로 지정한다.
# *_test.py 는 python 3.8 버전 이상부터 적용된다.
# 클래스 명칭
# class Test* 형식으로 지정한다.
# 클래스 메서드 및 함수 명칭
# def test_* 형식으로 지정한다.
def inc(x):
    return x + 1

# 테스트 실행 함수
def test_answer1():
    assert inc(3) == 5

def test_answer2():
    assert inc(3) == 4