# 9012.py
# 괄호

t = int(input())

for _ in range(t):
    ps = input()
    
    s = []
    for i in ps:
        if i == '(':
            s.append(i)
        elif i == ')':
            if len(s) == 0:
                s.append(i)
                break
            else:
                s.pop()
                
    if len(s) == 0:
        print('YES')
    else:
        print('NO')