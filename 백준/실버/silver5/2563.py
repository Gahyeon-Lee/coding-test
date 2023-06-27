# 2563.py
# 색종이

# array 내의 요소들은 각각 도화지를 1/100으로 나눈 한 칸을 의미
area = [[0] * 100 for _ in range(100)] 

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            area[i][j] = 1 # 각각의 색종이가 차지하는 부분의 요소값을 1로 바꿈

answer = 0
for i in area:
    answer += i.count(1)
print(answer)