# 7-7.py
# 집합 자료형 이용

# set() 함수 집합 자료형을 초기화할 때 사용: 단순히 특정한 데이터가 존재하는지 검사할 때에 효과적으로 사용 가능

n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')