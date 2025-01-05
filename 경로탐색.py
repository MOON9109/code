import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int, input().split(' '))
map_list=[[0]*(N+1) for _ in range(N+1)]
# print(map_list)
check=[0]*(N+1)
#print(map_list)
for i in range(M):
    s,d=map(int, input().split(' '))
    map_list[s][d]=1


def dfs(v):
    global count

    if v==N:
        count=count+1
        #print(result)

        return

    else:
        for i in range(1,N+1):
            if check[i]==0 and map_list[v][i]==1:
                #print(v,i)
                check[i] = 1
                result.append(i)
                dfs(i)
                check[i] = 0
                result.pop()



# check=[0]*(N+1)
#
# result=[0]*(N+1)









if __name__=='__main__':
    #print(map_list)
    check[1]=1
    count=0
    result = [1]
    dfs(1)



    # result[0]=1
    # dfs(1,N,1)
    print(count)









