# itertools - combinations_with_replacement (조합)
# 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
# 문제: 리스트 ['A', 'B', 'C']에서 '중복을 포함하여' 2개(r = 2)를 뽑아 순서에 상관없이 나열하는 모든 경우

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))

print(result)