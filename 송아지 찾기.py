import sys
#sys.stdin=open("input.txt","rt")
S,E=map(int, input().split(' '))
queue=[]
queue.append(S)


check=[0]*10001
dis=[0]*10001
check[S]=1



if __name__=='__main__':

    while ((len(queue) > 0)):
        x = queue.pop(0)

        #print(node,x)
        if x == E :
            print(dis[x])
            break
        else:


            for step in [1, -1, 5]:
                next_step = x + step
                if next_step>=1 and  next_step<=10000 and check[next_step]==0:
                    check[next_step] = 1
                    dis[next_step]=dis[x]+1
                    queue.append(next_step)












