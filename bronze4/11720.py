# 숫자의 합
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.

num = int(input())
N = input()

sum = 0

for i in N:
    sum += int(i)

print(sum)