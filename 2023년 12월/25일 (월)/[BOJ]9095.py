# 9095.py
# 1, 2, 3 더하기

# 이거 누적합이지요? 첫 번째에는 한 개, 두 번째에는 두 개, 세 번째에는 네 개, 네 번째에는 일곱 개
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]
            
t = int(input())

for _ in range(t):
    n = int(input())
    print(d[n])