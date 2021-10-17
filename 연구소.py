import copy


n, m=map(int, input().split(' '))

#상하좌우
dx=[0,0 ,-1, 1]
dy=[1,-1,0,0]

ma=[list(map(int,input().split())) for _ in range(n)]

ma2=copy.deepcopy(ma)

def virus(x, y, ma4):
    ma4[x][y]=2
    for i in range(4):
        
        nx= dx[i]+x
        ny=dy[i]+y
    
        if (0<= nx<n )and(0<= ny<m):
            if ma4[nx][ny]==0:
              
                virus(nx,ny,ma4)
                
area=0

def wall(start, count):
    global area
    if count==3:
        
        
        ma4=copy.deepcopy(ma2)
        for c in range(n):
            for d in range(m):
               
                if ma4[c][d]==2:
                    virus(c, d,ma4)
        temp = sum(_.count(0) for _ in ma4)
        
        area=max(temp, area)
        return
                    

    else:
        
        for i in range(start, n*m):
            a=(i//m)
            b=(i%m)
           
            if ma2[a][b]==0:
                ma2[a][b]=1
                wall(i, count+1)
                ma2[a][b]=0
wall(0,0)

print(area)
                








        
    
