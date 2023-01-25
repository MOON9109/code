def solution(participant, completion):
    d={}
    
    for x in participant:
        d[x]=d.get(x,0)+1 #키가 없으면 get 출력 0, 있으면 해당값 
    for y in completion:
        d[y]=d[y]-1
    result=[k for k,v in d.items() if v>0]
    answer=result[0]
    return answer
