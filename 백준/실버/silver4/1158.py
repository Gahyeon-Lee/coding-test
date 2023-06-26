# 1158.py
# 요세푸스 문제

"""from collections import deque

n, k = map(int, input().split())

q = deque(range(1 , n + 1))
answer = []

while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    answer.append(q.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))"""


# 또 다른 방법
# 약 46.8배 빠르다...

n, k = map(int, input().split())

q = [i for i in range(1, n + 1)]
answer = [] # 제거된 사람들을 넣을 배열
num = 0 # 제거될 사람의 인덱스 번호

for i in range(n):
    # 인덱스가 (k - 1)인 곳을 제거
    num += k - 1
    
    # 만약 num이 리스트의 길이보다 크거나 같으면 그 값을 리스트의 길이로 나눈 나머지 값으로 설정
    if num >= len(q): # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num %= len(q)
    answer.append(str(q.pop(num)))

print("<", ', '.join(answer), ">", sep="")