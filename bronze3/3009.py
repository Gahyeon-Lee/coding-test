# 네 번째 점
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 직사각형의 네 번째 점의 좌표를 출력한다.

xs = []
ys = []

for i in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

for i in range(3):
    if xs.count(xs[i]) == 1: 
        x = xs[i]
    if ys.count(ys[i]) == 1:
        y = ys[i]

print(x, y)