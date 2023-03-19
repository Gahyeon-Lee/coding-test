# collections - deque
# 첫 번째 원소를 삭제할 때 - popleft()
# 마지막 원소를 제거할 때 - pop()
# 첫 번째 인덱스에 원소 x를 삽입할 때 appendleft(x)
# 마지막 인덱스에 원소를 삽입할 때 append(x)

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))