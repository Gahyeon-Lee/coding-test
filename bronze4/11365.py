# !밀비 급일
# 한 줄에 하나의 암호가 주어진다. 암호의 길이는 500을 넘지 않는다.
# 마지막 줄에는 "END"가 주어진다. (END는 해독하지 않는다.)
# 각 암호가 해독된 것을 한 줄에 하나씩 출력한다.

while True:
    code = input()
    
    if code == "END":
        break
    
    print(code[::-1])