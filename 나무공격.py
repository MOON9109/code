import sys

n, m = map(int, input().split())
# print(n,m)

map_list = [[] for _ in range(n)]
result = 0
for i in range(n):
    map_list[i] = list(map(int, input().split()))
    result = result + sum(map_list[i])
# print(map_list)
L1, R1 = map(int, input().split())
# print(L1,R1)
L2, R2 = map(int, input().split())


# print(L2,R2)

def attack_function(L, R, map_list):
    global result
    for i in range(L - 1, R):
        for j in range(m):
            if map_list[i][j] != 0:
                map_list[i][j] = 0
                result = result - 1
                break

    # return map_list


attack_function(L1, R1, map_list)
attack_function(L2, R2, map_list)

print(result)