# itertools - permutations (순열)
# 문제: 리스트 ['A', 'B', 'C']에서 3개(r = 3)를 뽑아 나열하는 모든 경우

from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))

print(result)