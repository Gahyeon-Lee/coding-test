# 14425.py
# 문자열 집합

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = set()

for _ in range(n):
    s.add(input().rstrip())

total = 0
for _ in range(m):
    word = input().rstrip()
    if word in s:
        total += 1
        
print(total)