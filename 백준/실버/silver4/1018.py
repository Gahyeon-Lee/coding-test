# 1018.py
# 체스판 다시 칠하기

n, m = map(int, input().split())

matrix = []
count = []

for i in range(n):
    matrix.append(input())

for a in range(n - 7):
    for b in range(m - 7):
        w_index = 0
        b_index = 0
        
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if matrix[i][j] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if matrix[i][j] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        count.append(w_index)
        count.append(b_index)
print(min(count))