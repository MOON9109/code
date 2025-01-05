import sys
#sys.stdin=open("input.txt","rt")
N, M=map(int,input().split(" "))

res=[0]*M
count=0
def dfs(k,M):
    global count
    if k==(M):
        for j in range(len(res)):
            print(res[j],end=' ')
        print()
        count=count+1

    else:
        for i in range(1,N+1):
            if res[k]==0:
                res[k]=i
                dfs(k+1,M)
                res[k]=0

if __name__=='__main__':
    dfs(0, M)
    print(count)






