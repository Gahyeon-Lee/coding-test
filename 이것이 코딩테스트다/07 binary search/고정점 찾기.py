# 고정점 찾기
# 난이도 1.5 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB

n = int(input())
array = list(map(int, input().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if mid == array[mid]:
            return mid
        elif mid > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return None

result = binary_search(array, 0, n - 1)

if result == None:
    print(-1)
else:
    print(result)
    

"=============================="
"아래는 교재 정답"
"교재는 재귀함수를 사용함"

def binary(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary(array, start, mid - 1)
    else:
        return binary(array, mid + 1, end)
    
n = int(input())
array = list(map(int, input().split()))

index = binary(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)