# 11653.py
# 소인수분해

n = int(input())

factorization = []
i = 2
while i <= n:
    if n % i == 0:
        factorization.append(i)
        n //= i
    else:
        i += 1

for i in factorization:
    print(i)