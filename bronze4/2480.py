# 주사위 세개
# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다. 
# 첫째 줄에 게임의 상금을 출력 한다.

dice1, dice2, dice3 = map(int, input().split())

if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)
elif dice1 == dice2 or dice1 == dice3:
    print(1000 + dice1 * 100)
elif dice2 == dice3:
    print(1000 + dice2 * 100)
else:
    print(max(dice1, dice2, dice2) * 100)
    