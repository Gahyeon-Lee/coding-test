# 1874.py
# 스택 수열

n = int(input())

data = []
stack = []
now = 1
find = True

for _ in range(n):
    num = int(input())
    
    while now <= num:
        stack.append(now)
        data.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        data.append('-')
    else:
        find = False
    
if not find:
    print('NO')
else:
    for i in data:
        print(i)