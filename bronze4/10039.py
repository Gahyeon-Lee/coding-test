# 평균 점수
# 입력은 총 5줄로 이루어져 있고, 원섭이의 점수, 세희의 점수, 상근이의 점수, 숭이의 점수, 강수의 점수가 순서대로 주어진다.
# 점수는 모두 0점 이상, 100점 이하인 5의 배수이다. 따라서, 평균 점수는 항상 정수이다. 
# 첫째 줄에 학생 5명의 평균 점수를 출력한다.

total = 0

for _ in range(5):
    scores = int(input())
    
    if scores < 40:
        scores = 40
    
    total += scores

print(total // 5)
    