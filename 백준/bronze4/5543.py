# 상근날드
# 입력은 총 다섯 줄이다. 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 셋째 줄에는 하덕버거의 가격이 주어진다. 
# 넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다의 가격이 주어진다. 모든 가격은 100원 이상, 2000원 이하이다.
# 첫째 줄에 가장 싼 세트 메뉴의 가격을 출력한다.

burger = []
for _ in range(3):
    burger.append(int(input()))
    
baverage = []
for _ in range(2):
    baverage.append(int(input()))
    
print(min(burger) + min(baverage) - 50)