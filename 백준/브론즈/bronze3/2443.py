# 별 찍기 - 6
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num = int(input())

for i in range(num, 0, -1):
    print(' ' * (num - i) + '*' * (2 * i - 1))