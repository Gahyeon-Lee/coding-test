# 9093.py
# 단어 뒤집기

# 내가 짠 코드에 sys 추가

import sys

t = int(input())

for _ in range(t):
    s = list(sys.stdin.readline().rstrip().split())
    words = []
    
    for i in s:
        words.append(i[::-1])
    
    print(' '.join(words))
    
    
"""
    t = int(input())

    for _ in range(t):
        s = list(map(str, input().split()))
    
        for i in range(len(s)):
            s[i] = s[i][::-1]
    
        for i in s:
            print(i, end=' ')
        print()
"""