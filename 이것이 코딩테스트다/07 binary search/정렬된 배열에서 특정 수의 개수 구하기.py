# 정렬된 배열에서 특정 수의 개수 구하기
# 난이도 2 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

def count_by_value(array, x):
    n = len(array)
    
    a = first(array, x, 0, n - 1)
    
    if a == None:
        return 0
    
    b = last(array, x, 0, n - 1)
    
    return b - a + 1

# 처음 위치를 찾는 함수
def first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
        if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

# 마지막 위치를 찾는 함수
def last(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
        if (mid == n - 1 or target < array[mid - 1]) and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)