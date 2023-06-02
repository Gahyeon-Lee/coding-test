# 2581.py
# 소수

m = int(input())
n = int(input())

prime = []
for i in range(m , n + 1):
    check = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            prime.append(i)
        
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))