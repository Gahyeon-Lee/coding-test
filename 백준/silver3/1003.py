# 1003.py
# 피보나치 함수

t = int(input())

for _ in range(t):
    n = int(input())
    
    zero, one = 1, 0 # zero: 0개수, one: 1개수
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)