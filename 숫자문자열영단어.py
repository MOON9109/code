def solution(s):
    
    number={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}  
    
    answer=""
    temp=""
    
    for x in s:
        
        if x>='0' and x<='9':
            answer=answer+x
        else:
            temp=temp+x
            if temp in number.keys():
                answer=answer+number[temp]
                temp=""            
            
            
    return int(answer)
