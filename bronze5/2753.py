# 윤년
# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
# 첫째 줄에 윤년이면 1, 아니면 0을 출력한다.

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("1")
else:
    print("0")