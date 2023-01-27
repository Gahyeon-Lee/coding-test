# 8-1.py
# 피보나치 함수 소스코드

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# O(2^N) 
# N이 커질수록 너무 긴 시간이 소요됨