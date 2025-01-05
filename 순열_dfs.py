import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int, input().split(' '))

check=(N+1)*[0]
res=[0]*N

def dfs(k,M):
    global count
    if k==M:
        for j in range(len(res)):
            if res[j]!=0:
                print(res[j],end=' ')
        count=count+1
        print()
        return
    else:

        for i in range(1,N+1):
            if check[i]==0:
                check[i]=1
                res[k]=i
                dfs(k+1,M)
                check[i] = 0
                res[k] = 0







if __name__=='__main__':
    count=0
    dfs(0,M)
    print(count)








