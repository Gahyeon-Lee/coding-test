# 안테나
# 난이도 1 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 256MB

n = int(input())
data = list(map(int, input().split()))

answer = []
data.sort()

for i in range(n):
    total = 0
    for j in range(n):
        if data[i] > data[j]:
            total += data[i] - data[j]
        else:
            total += data[j] - data[i]
    answer.append((data[i], total))

answer.sort(key=lambda x: x[1])
print(answer[0][0])


"=============================="
"아래는 교재 정답"

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])