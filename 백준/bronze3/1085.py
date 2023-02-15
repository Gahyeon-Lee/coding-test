# 직사각형에서 탈출
# 첫째 줄에 x, y, w, h가 주어진다.
# 첫째 줄에 문제의 정답을 출력한다.

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))