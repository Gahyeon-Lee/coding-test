# 12605.py
# 문자열 뒤집기

n = int(input())

for i in range(n):
    s = list(input().split())
    print("Case #%d: " %(i + 1), end='')
    for j in s[::-1]:
        print(j, end=' ')
    print()