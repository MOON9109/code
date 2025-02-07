H, K, R = map(int, input().split())
work = [list(map(int, input().split())) for _ in range(2 ** H)]
people = 2 ** (H + 1) - 1  # 직원 숫자
company = [[] for _ in range(people + 1)]
bottom = 2 ** (H)  # 말단 직원 숫자
not_bottom = 2 ** (H) - 1  # 말단 직원이 아닌 직원의 숫자

for idx in range(bottom):  # 업무 할당
    company[people - idx] = work[-1 - idx]

# print(company)

result = 0

for r in range(R):
    for i in range(1, not_bottom + 1):
        if i == 1:
            if len(company[1]) > 0:  # 부서장의 업무 중 처리된 업무가 있다면 그 번호를 더함
                result = result + company[1].pop(0)

        # print(r)
        if r % 2 == 0:  # 날짜가 짝수일 때
            if len(company[2 * i + 1]) > 0:
                value = company[2 * i + 1].pop(0)
                company[i].append(value)
                # print(i,value)
        elif r % 2 == 1:  # 날짜가 홀수일 때
            if len(company[2 * i]) > 0:
                value = company[2 * i].pop(0)
                company[i].append(value)
                # print(i,value)
print(result)
