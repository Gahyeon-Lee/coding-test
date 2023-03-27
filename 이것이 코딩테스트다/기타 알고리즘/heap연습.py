# 힙(Heap)에 대해 공부

import heapq

print("----------------최소힙-------------------")

# 최소힙
min_heap = []

for i in range(1, 6):
    heapq.heappush(min_heap, i)

for i in range(5):
	print(heapq.heappop(min_heap))
 

print("\n----------------최대힙-------------------")
 
# 최대힙
# heapq에서는 최대 힙을 제공하지 않는다. 
# 따라서 다음과 같이 부호를 변경하는 방법을 사용해서 최대 힙을 구현한다. 
# 부호를 바꿔서 최소 힙에 넣어준 뒤에 최솟값부터 pop을 해줄 때 다시 부호를 바꿔주면 최대 힙과 동일하다.
max_heap = []
values = [1,5,3,2,4]
 
for value in values:
    heapq.heappush(max_heap, -value)

for i in range(5):
    print(-heapq.heappop(max_heap))