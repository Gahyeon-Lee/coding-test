# 6-11.py
# 성적이 낮은 순서로 학생 출력하기

n = int(input())

score = []
for _ in range(n):
    info = input().split()
    score.append((info[0], int(info[1])))

score = sorted(score, key=lambda student:student[1])

for i in score:
    print(i[0], end=' ')
    
"""
def 함수이름(매개변수): lamda 매개변수: 결과
return 결과 
"""