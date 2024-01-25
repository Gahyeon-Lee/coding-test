# 5430.py
# AC

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().strip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    check = False
    count = 0
    
    if n == 0:
        arr = deque()

    for command in p:
        if command == 'R':
            count += 1
        elif command == 'D':
            if not arr:
                check = True
                break
            else:
                if count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
                    
    if check == True:
        print("error")
    else:
        if count % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')