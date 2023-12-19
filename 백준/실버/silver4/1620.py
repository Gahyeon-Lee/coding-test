# 1620.py
# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pocket_monster = {}

for i in range(1, n + 1):
    name = input().rstrip()
    
    pocket_monster[name] = i
    pocket_monster[i] = name
        
for _ in range(m):
    q = input().rstrip()
    
    if q.isdigit():
        print(pocket_monster[int(q)])
    else:
        print(pocket_monster[q])