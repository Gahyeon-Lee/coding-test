# 모험가 길드

n = int(input())
horror = list(map(int, input().split()))

horror.sort()
count = 0
result = 0

for i in horror:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

# 아이디어는 있는데 코딩으로 구현을 못 하는 게 현 문제점인 것인가...ㅠㅠ (멍청이, 말미잘, ...)