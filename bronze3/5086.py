# 배수와 약수
# 입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 
# 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while True:
    num1, num2 = map(int, input().split())
    
    if num1 == num2 == 0:
        break
    
    if num1 % num2 == 0:
        print("multiple")
    elif num2 % num1 == 0:
        print("factor")
    else:
        print("neither")