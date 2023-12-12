# 1439.py
# 뒤집기

s = input()

zero = 0
one = 0

for i in range(len(s) - 1):
    if s[i] == '0' and s[i] != s[i + 1]:
        zero += 1
    elif s[i] == '1' and s[i] != s[i + 1]:
        one += 1
    else:
        continue

if s[-1] == '0':
    zero += 1
else:
    one += 1
    
print(min(zero, one))