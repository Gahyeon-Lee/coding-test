# 2775.py
# 부녀회장이 될테야

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    
    d = [0] * (n + 1)
    for j in range(1, n + 1):
        d[j] = j
        
    for m in range(k):
        for n in range(1, n + 1):
            d[n] += d[n - 1]
            
print(d[-1])