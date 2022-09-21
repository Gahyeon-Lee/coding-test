# 합
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

num = int(input())
sum = 0

for i in range(1, num+1):
    sum += i
print(sum)