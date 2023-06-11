# 만들 수 없는 금액
# 난이도1 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

import itertools

n = int(input())
data = list(map(int, input().split()))

results = []
for i in range(1, sum(data) + 1):
    results.append(i)
    
for i in range(1, n + 1):
    for j in itertools.permutations(data, i):
        result = sum(list(j))
        
        if result in results:
            results.remove(result)
            
print(min(results))


# =============== 풀이 및 정답 =================
# 1. 정렬을 이용한 그리디 알고리즘, 화폐 단위를 기준으로 오름차순으로 정렬 (1부터 차례대로 특정 금액을 만들 수 있는지 확인)
# 2. 1부터 target - 1까지 모든 금액을 만들 수 있다고 가정
# 3. 만약 target 금액을 만들 수 있다면 target 값을 증가

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1  # 금액 1을 만들 수 있는지 확인하기 위해 설정
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target) 