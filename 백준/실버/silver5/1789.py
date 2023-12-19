# 1789.py
# 수들의 합

# 접근법
# 1. 가장 작은 수부터 더해가면 됨

s = int(input())

num = 0
for i in range(1, s + 1):
    num += i
    
    if num >= s:
        print(i - 1)
        break