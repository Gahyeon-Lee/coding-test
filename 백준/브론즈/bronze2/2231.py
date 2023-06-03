# 2231.py
# 분해합

n = int(input())

for i in range(1, n + 1):
    num = list(str(i))
    total = i + sum(map(int, num))
    
    if total == n:
        print(i)
        break
    
    if i == n: # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)


# 내가 푼 게 왜인지는 더 빨랐지만...        
"""
n = int(input())

division = []
for i in range(1, n):
    num = list(str(i))
    total = i + sum(map(int, num))
    
    if total == n:
        division.append(i)

if len(division) == 0:
    print(0)
else:
    print(min(division))
"""