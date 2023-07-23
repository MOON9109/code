#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import heapq
#input = sys.stdin.readline


def heapsort(iterable):
    h=[]
    result=[]
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


# In[4]:


n= int(input())


# In[5]:


arr=[]


# In[6]:


print(f"{n}개 숫자를 입력하세요")

for i in range(n):
    
    arr.append(int(input()))
    
res= heapsort(arr)
print("최소힙 정렬은 다음과 같이 나옵니다")
for i in range(n):
    
    print(res[i])


# In[ ]:




