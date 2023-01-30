# 7-5.py
# 부품 찾기

# 내가 푼 방식 - 반복문을 이용

n = int(input())
total = list(map(int, input().split()))

m = int(input())
part = list(map(int, input().split()))

def binary_search(total, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if total[mid] == target:
            return mid
        elif total[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    result = binary_search(total, part[i], 0, n - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')