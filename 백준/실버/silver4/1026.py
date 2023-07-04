# 1026.py
# 보물

# s의 값이 최소가 되어야 하므로 A는 오름차순으로, B는 내림차순으로 정렬해서 곱하면 되지 않을까?

# 방법 1) b를 재배열하는 방식
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

s = 0
for i in range(n):
    s += (a[i] * b [i])
print(s)

# 방법 2) b를 재배열하지 않는 방식
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(s)