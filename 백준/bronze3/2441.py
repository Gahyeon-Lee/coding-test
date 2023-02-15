# 별 찍기 - 5
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * i)