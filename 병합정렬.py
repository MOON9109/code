# 병합 정렬

# 분할 정복(divide & conquer) 방식을 이용
# 절반씩 합치면서 정렬하면 , 전체 리스트가 정렬됨
# 시간 복잡도 O(NlogN)을 보장

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) //2
    left =merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <right[j]:
            array[k] =left[i]
            i +=1
        else:
            array[k] = right[j]
            j +=1
        k += 1

    if i == len(left):
        while j< len(right):
            array[k] = right[j]
            j +=1
            k +=1
    elif j == len(right):
            while i< len(left):
                array[k] =left[i]
                i +=1
                k +=1

    return array

n = int(input())
array =[]
for _ in range(n):
    array.append(int(input()))
array = merge_sort(array)

for data in array:
    print(data)
