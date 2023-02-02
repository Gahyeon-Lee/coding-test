# 10-2.py
# 경로 압축 기법 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# find 함수 호출 이후에 해당 노드의 루트 노드가 바로 부모드가 됨