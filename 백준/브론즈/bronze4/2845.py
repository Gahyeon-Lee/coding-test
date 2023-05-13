# 파티가 끝나고 난 뒤
# 첫째 줄에 1m2당 사람의 수 L (1 ≤ L ≤ 10)과 파티가 열렸던 곳의 넓이 P (1 ≤ P ≤ 1000)가 주어진다.
# 둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다. 106보다 작은 양의 정수 5개가 주어진다.
# 출력은 첫째 줄에 다섯 개의 숫자를 출력해야 한다. 
# 이 숫자는 상근이가 계산한 참가자의 수와  각 기사에 적혀있는 참가자의 수의 차이이다.

people, area = map(int, input().split())
articles = list(map(int, input().split()))

total_people = people * area

for i in articles:
    print(i - total_people, end=' ')