# 11508.py
# 2 + 1 세일

n = int(input())

price = []
for _ in range(n):
    price.append(int(input()))
    
price.sort(reverse=True)

answer = []
chunks = [price[i:i+3] for i in range(0, n, 3)]

for chunk in chunks:
    if len(chunk) == 3:
        answer.append(sum(chunk) - min(chunk))
    else:
        answer.append(sum(chunk))
    
print(sum(answer))


# 이 로직은 chat GPT의 도움을 받았기 때문에 더 분발합시다.
# 그렇게 어려운 거는 아닌데...내가 멍청해서...
# 슬라이싱이 이렇게 중요합니다. 여러분.
