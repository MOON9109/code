import sys
#sys.stdin=open("input.txt","rt")
C, N=map(int,input().split(" "))
#print(C,N)
Weight_list=[0]*(N)
for i in range(N):
    Weight_list[i]=int(input())




def dfs(k,sum, tsum):
    global answer
    if sum+total-tsum<answer:
        return

    if sum>C:
        return

    if k==N:
        #print(sum)
        if answer<sum:
            answer=sum

        return
    else:

        dfs(k+1,sum+Weight_list[k],tsum+Weight_list[k])
        dfs(k+1,sum,tsum+Weight_list[k])
if __name__=='__main__':


    answer=0
    total=sum(Weight_list)
    dfs(0,0,0)
    print(answer)







