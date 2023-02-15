# 방학 숙제
# 한 줄에 하나씩 총 다섯 줄에 걸쳐 L, A, B, C, D가 주어진다. (2 ≤ L ≤ 40, 1 ≤ A, B ≤ 1000, 1 ≤ C, D ≤ 100)
# 항상 방학 숙제를 방학 기간내에 다 할 수 있는 경우만 입력으로 주어진다.
# 첫째 줄에 상근이가 놀 수 있는 날의 최댓값을 출력한다.

from math import ceil


vacation = int(input())
math = int(input())
korean = int(input())
math_own = int(input())
korean_own = int(input())

math_all = ceil(math / math_own)
korean_all = ceil(korean / korean_own)

rest_vacation = max(math_all, korean_all)
print(vacation - rest_vacation)