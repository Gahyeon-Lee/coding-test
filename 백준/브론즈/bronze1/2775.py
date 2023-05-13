# 2775.py
# 부녀회장이 될테야

t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    
    d = [i for i in range(1, n + 1)]
        
    for m in range(k):
        for b in range(1, n):
            d[b] += d[b - 1]
            
    print(d[-1])