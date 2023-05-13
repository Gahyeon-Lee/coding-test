# 킹, 퀸, 룩 , 비숍, 나이트 , 폰

found_chess = list(map(int, input().split()))
need_list = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(need_list[i] - found_chess[i], end=' ')