# 14888.py
# 연산자 끼워넣기

n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9


def dfs(v, now, add, sub, mul, div):
    global max_value, min_value
    
    if v == n:
        max_value = max(now, max_value)
        min_value = min(now, min_value)
        return

    if add:
        dfs(v + 1, now + number[v], add - 1, sub, mul, div)
    if sub:
        dfs(v + 1, now - number[v], add, sub - 1, mul, div)
    if mul:
        dfs(v + 1, now * number[v], add, sub, mul - 1, div)
    if div:
        dfs(v + 1, int(now / number[v]), add, sub, mul, div - 1)


dfs(1, number[0], op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)