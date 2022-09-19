# 엄청난 부자2
# 첫째 줄에는 최백준 조교가 가진 돈 n과 돈을 받으러 온 생명체의 수 m이 주어진다.
# 첫째 줄에 생명체 하나에게 돌아가는 돈의 양을 출력한다. 
# 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력한다.

money, entity_num = map(int, input().split())

equal_divided = money // entity_num
rest = money % entity_num

print(equal_divided)
print(rest)