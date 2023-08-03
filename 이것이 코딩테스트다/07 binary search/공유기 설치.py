# 공유기 설치
# 난이도 2 | 풀이 시간 50분 | 시간 제한 2초 | 메모리 제한 128MB

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)