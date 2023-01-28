def solution(n, lost, reserve):
    
    st=[1]*(n+2)
    
    for x in reserve:
        st[x]=st[x]+1
    for y in lost:
        st[y]=st[y]-1
        
    for k in range(1,n+1):
        
        if st[k-1]==0 and st[k]==2:
            st[k-1]=1
            st[k]=1
        else:
            if st[k]==2 and st[k+1]==0:
                st[k]=1
                st[k+1]=1
    
    result=st[1:n+1]
    answer=0
    for x in result:
        if x>=1:
            answer=answer+1
        
    return answer
