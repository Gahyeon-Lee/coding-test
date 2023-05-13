# 지능형 기차
# 각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 
# 첫째 줄에 최대 사람 수를 출력한다. 

biggest = 0
num = 0

for i in range(4):
    x, y = map(int, input().split())
    
    num += y - x
    
    if num > biggest:
        biggest = num
        
print(biggest)