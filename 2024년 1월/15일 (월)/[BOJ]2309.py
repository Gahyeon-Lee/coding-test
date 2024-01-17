# 2309.py
# 일곱 난쟁이

height = []
for _ in range(9):
    n = int(input())
    height.append(n)

a, b = 0, 0
total = sum(height)
for i in range(8):
    for j in range(i + 1, 9):
        if total - (height[i] + height[j]) == 100:
            a, b = height[i], height[j]

height.remove(a)
height.remove(b)
height.sort()

for i in height:
    print(i)