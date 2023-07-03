# 1931.py
# 회의실 배정

# 그리디 문제니까 생각을 해보자면
# 1. 회의 시간이 가장 짧은 회의를 여러 개 배치하면 최대가 되겠다.
# 2. 빨리 끝나는 회의 순서대로 정렬
# 3. 끝나는 시간이 같다면 빨리 시작하는 순서대로 정렬
# 결론 - 먼저 시작시간을 오름차순으로 정렬한 뒤, 끝나는 시간을 기준으로 한번 더 정렬

n = int(input())

meeting = []
for _ in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

count = 0
time = 0 # 이전 회의의 끝나는 시간
for meet in meeting:
    if time <= meet[0]:
        time = meet[1]
        count += 1

print(count)