# itertools - product (순열)
# 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우, 원소를 중복하여 뽑음
# repeat: product 객체를 초기화할 때 뽑고자 하는 데이터의 수
# 문제: 리스트 ['A', 'B', 'C']에서 '중복을 포함하여' 2개(r = 2)를 뽑아 나열하는 모든 경우

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))

print(result)