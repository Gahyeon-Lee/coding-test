# 크냐?
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 두 정수가 주어진다. 
# 두 수는 백만보다 작거나 같은 양의 정수이다. 입력의 마지막 줄에는 0이 두 개 주어진다.
# 각 테스트 케이스마다, 첫 번째 수가 두 번째 수보다 크면 Yes를, 아니면 No를 한 줄에 하나씩 출력한다.

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    
    if num1 > num2:
        print("Yes")
    else:
        print("No")