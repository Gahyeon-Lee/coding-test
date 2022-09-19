# 사파리월드
# 첫째 줄에 두 도메인의 유명도 N과 M이 주어진다.
# 첫째 줄에 두 유명도의 차이 (|N-M|)을 출력한다.

num1, num2 = map(int, input().split())

print(abs(num1 - num2))