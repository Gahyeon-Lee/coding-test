# 2577.py
# 숫자의 개수

num = [0] * 10
total = 1

for _ in range(3):
    total *= int(input())

for i in str(total):
    num[int(i)] += 1
    
for i in num:
    print(i)