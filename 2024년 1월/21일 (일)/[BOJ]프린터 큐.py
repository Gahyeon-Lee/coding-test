# 1966.py
# 프린터 큐

from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    count = 0
    while q:
        max_value = max(q)
        
        if q[0] == max_value:
            q.popleft()
            if m == 0:
                count += 1
                break
            else:
                count += 1
                m -= 1 # 한 칸씩 당겨짐
        else:
            front = q.popleft()
            q.append(front)
            if m == 0:
                m += len(q) - 1
            else:
                m -= 1
    print(count)