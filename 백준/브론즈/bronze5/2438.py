# 별 찍기 - 1
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

line_num = int(input())

for i in range(1, line_num +1 ):
    print('*' * i)