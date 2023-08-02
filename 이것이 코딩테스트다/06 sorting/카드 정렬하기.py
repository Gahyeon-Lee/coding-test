# 카드 정렬하기
# 난이도 2 | 풀이 시간 30분 | 시간 제한 2초 | 메모리 제한 128MB

# 내가 푼 거 실수로 지워버려서 날라갔는데 heap을 사용해서 더 빠르게 구현할 수 있었음
# heap 사용한 거 빼면 로직 자체는 같았음

import heapq

n = int(input())

data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

result = 0

while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    
    sum_value = one + two
    result += sum_value
    heapq.heappush(data, sum_value)

print(result)