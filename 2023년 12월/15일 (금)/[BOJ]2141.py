# 2141.py
# 우체국

n = int(input())

info = []
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    info.append((x, a))
    people += a

info = sorted(info, key=lambda x: x[0])
now = 0
for i in range(n):
    now += info[i][1]
    
    if now >= people / 2:
        print(info[i][0])
        break