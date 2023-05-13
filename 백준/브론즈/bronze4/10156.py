# 과자
# 첫 번째 줄에는 과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M이 각각 공백을 사이에 두고 주어진다.
# 단, K, N은 1,000 이하의 양의 정수이고, M은 10만 이하의 양의 정수이다. (1 ≤ K, N ≤ 1,000, 1 ≤ M ≤ 100,000이다.) 
# 첫 줄에 동수가 부모님께 받아야 하는 돈의 액수를 출력한다. 

price, num, money = map(int, input().split())

total = (price * num) - money

if total > 0:
    print(total)
else:
    print(0)