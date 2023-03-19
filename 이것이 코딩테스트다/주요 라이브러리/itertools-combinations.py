# itertools - combination (조합)
# 문제: 리스트 ['A', 'B', 'C']에서 2개(r = 2)를 뽑아 나열하는 모든 경우

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))

print(result)