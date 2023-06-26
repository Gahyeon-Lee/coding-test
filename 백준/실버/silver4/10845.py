# 10845.py
# 큐

from collections import deque
import sys

n = int(input())
q = deque([])

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        q.append(int(command[1]))
    elif command[0] == 'pop':
        if q:
            print(q.popleft())  # deque 안 쓰고 pop(0) 쓸 수 있는데 시간 복잡도가 더 높아서 dqeue 쓰는 게 안전함
        else:
            print(-1)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1) 
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)