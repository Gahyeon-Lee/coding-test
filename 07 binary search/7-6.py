# 7-6.py
# 계수 정렬을 이용한 풀이

n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')