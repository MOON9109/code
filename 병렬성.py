# Future 동시성
# 비동기 작업 실행

# 동기 A->B A 마치고 B실행
# 비동기 둘다 걸어둠

# 지연시간 (Block) CPU 및 리소스 낭비 방지 -> (File) Network I/O 관련 작업 -> 동시성 활용 권장

# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# 1.멀티스레딩/ 멀티프로세싱 API 통일 -> 매우 사용하기 쉬움

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2


# GIL (파이썬에만 있음)
# 쓰레드 사용한다고 좋은 것이 아님
# GIL : 두개 이상의 스레드가 동시에 실행 될때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해
#    GIL 실행, 리소스 전체에 락이 걸린다. ->  Context Switch (문맥 교환)

# GIL : 멀티프로세싱 사용, CPython 사용


import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 100000000]


# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (제너레이터)

def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # worker count
    worker = min(10, len(WORK_LIST))
    print(worker)
    # 시작 시간
    start_tm = time.time()
    #ProcessPoolExecutor()

    with futures.ThreadPoolExecutor() as excutor:
        #map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm

    print(result)

    # 출력 포맷
    msg = f"\n Result -> {list(result)} Time : {end_tm}s"
    print(msg)

if __name__ == '__main__':
    main()
