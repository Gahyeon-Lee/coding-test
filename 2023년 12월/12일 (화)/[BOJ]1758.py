# 1758.py
# 알바생 강호

n = int(input())

tip = []
for _ in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

# 원래 주려던 돈 - (등수 - 1)
total = 0
for i in range(n):
    value = tip[i] - i
    
    if value < 0:
        value = 0 # 여기를 그냥 continue로 해도 될 듯
        
    total += value
    value = 0

print(total)