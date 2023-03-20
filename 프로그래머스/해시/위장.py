# 위장
# 안 보고 다시 풀어보기
# 예시 
"""
    1. [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    2. [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
"""

def soulution(clothes):
    answer = 1
    items = {}
    
    for item, category in clothes:
        if category not in items:
            items[category] = []
        items[category].append(item)
    
    for i in items.keys():
        answer *= len(items[i]) + 1
    return answer - 1

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(soulution(clothes))

"""
    [헤삭]
    1. 각 종류 마다의 경우의 수 + 아무 것도 안 입는 경우(1)
    2. 각 종류 마다의 경우의 수를 전부 다 곱하면 전체의 경우의 수가 나옴
    3. 전체의 경우에서 아무 것도 안 입는 경우의 수는 언제나 1개이고 그 1을 빼면 입을 수 있는 모든 경우의 수가 나옴
"""