# 윷 놀이
# 첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가 빈칸을 사이에 두고 주어진다.
# 첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.

for _ in range(3):
    yuts = list(map(int, input().split()))
    
    num = yuts.count(0)
    
    if num == 1:
        print('A')
    elif num == 2:
        print('B')
    elif num == 3:
        print('C')
    elif num == 4:
        print('D')
    else:
        print('E')