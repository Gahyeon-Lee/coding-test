# 심부름 가는 길
# 입력은 총 4줄이며, 한 줄에 하나씩 양의 정수가 적혀있다.
# 집에 늦게 가면 혼나기 때문에, 총 이동시간은 항상 1 분 0 초 이상 59 분 59 초 이하이다.
# 총 이동시간 x 분 y 초를 출력한다. 첫 번째 줄에 x를, 두 번째 줄에 y를 출력한다.

from math import floor


to_school = int(input())
to_pc = int(input())
to_hakwon = int(input())
to_house = int(input())

total_time = to_school + to_pc + to_hakwon + to_house

minute = floor(total_time / 60)
second = total_time - minute * 60

print(minute)
print(second)