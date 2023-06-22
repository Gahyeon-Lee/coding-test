# 2075.py
# N번째 큰 수

import heapq

n = int(input())
board = []

for _ in range(n):
    nums = list(map(int, input().split()))
    
    if not board:
        for num in nums:
            heapq.heappush(board, num)
    else:
        for num in nums:
            if num > board[0]:
                heapq.heappush(board, num)
                heapq.heappop(board)
print(board[0])