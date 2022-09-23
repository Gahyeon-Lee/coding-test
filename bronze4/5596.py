# 시험 점수
# 1번째 줄에는 순서대로 민국이의 정보, 수학, 과학, 영어 점수(정수형)가 있으며, 공백으로 구분되어 있다.
# 2번째 줄에는 1번째 줄과 마찬가지로 순서대로 만세의 정보, 수학, 과학, 영어 점수(정수형)가 있고, 공백으로 구분되어 있다.
# 문제에서 요구하는 정답을 출력한다.

minguk = sum(list(map(int, input().split())))
manse = sum(list(map(int, input().split())))
    
print(max(minguk, manse))