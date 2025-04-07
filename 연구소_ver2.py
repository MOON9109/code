from itertools import combinations
import copy
from collections import deque
N, M= map(int,input().split(' '))
Map=[]
emptyList=[]
VirusList=[]

moves=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(VirusList,copied_map):
    q=deque(VirusList)

    while q:
        x,y=q.popleft()
        for move in moves:
            nx=x+move[0]
            ny=y+move[1]

            if (0<=nx<N) and (0<=ny<M):
                if copied_map[nx][ny]==0:
                    copied_map[nx][ny]=2
                    q.append([nx,ny])
    return copied_map

def count_zero(map_result):
    count=0
    for row in map_result:
        count=count+row.count(0)

    return count




for i in range(int(N)):
    temp=list(map(int,input().split(' ')))
    Map.append(temp)

    for j in range(int(M)):
        if int(temp[j])==0:
            emptyList.append([i,j])
        elif int(temp[j])==2:
            VirusList.append([i,j])


wallList=combinations(emptyList,3)


#
# print(Map)
# print(emptyList)
# print(wallList)
answer=0
for Wall in wallList:
    # print(f'Wall:{Wall}')
    X1,Y1=Wall[0]
    X2,Y2=Wall[1]
    X3,Y3=Wall[2]

    # print(X1,Y1)
    # print(X2,Y2)
    # print(X3,Y3)

    copied_map=copy.deepcopy(Map)
    copied_map[X1][Y1]= 1
    copied_map[X2][Y2]= 1
    copied_map[X3][Y3]= 1
    map_result=bfs(VirusList, copied_map)
    result=count_zero(map_result)
    if answer<=result:
        answer=result
print(answer)

