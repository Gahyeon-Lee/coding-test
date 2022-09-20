# 학점계산
# 첫째 줄에 C언어 성적이 주어진다. 성적은 문제에서 설명한 13가지 중 하나이다.
# 첫째 줄에 C언어 평점을 출력한다.

score = input()

if len(score) == 1:
    down = 0.0
elif score[1] == '+':
    down = 0.3
elif score[1] == '0':
    down = 0.0
else:
    down = -0.3

if score[0] == 'A':
    result = 4 + down
elif score[0] == 'B':
    result = 3 + down
elif score[0] == 'C':
    result = 2 + down
elif score[0] == 'D':
    result = 1 + down
else:
    result = 0.0

print(result)