# 홀수
# 입력의 첫째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.
# 홀수가 존재하지 않는 경우에는 첫째 줄에 -1을 출력한다. 
# 홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최솟값을 출력한다.

odds = []

for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        odds.append(num)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)    