import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
Money=list(map(int, input().split(' ')))
M=int(input())

def dfs(K,N,M):
    global answer
    if answer<N:
        return

    if K>=M:
        if (answer > N )and  (K==M):
            answer = N
        return


    else:

        for value in Money:
            dfs(K+value,N+1,M)



if __name__=='__main__':

    answer=9999

    Money.sort(reverse=True)

    dfs(0,0,M)
    print(answer)








