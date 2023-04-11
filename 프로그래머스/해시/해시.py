# 해시 연습
# 딕셔너리를 통해서 구현
'''
    언제 사용하는가?
    1. 리스트를 쓸 수 없을 때
    2. 빠른 접근 / 탐색이 필요할 때
    3. 집계가 필요할 때
'''

hash_table = [0 for _ in range(100)]

def hash_function(key):
    # 파이썬 내장함수 hash 사용
    return hash(key) % 100

def set_data(key, value):
    hash_value = hash_function(key)
    hash_table[hash_value] = value
    
def get_data(key):
    hash_value = hash_function(key)
    return hash_table[hash_value]

set_data('Red', 2022)
set_data('hello', 77)
print(get_data('Red'))
print(get_data('hello'))