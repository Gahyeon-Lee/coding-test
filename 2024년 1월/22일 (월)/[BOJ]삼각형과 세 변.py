# 5073.py
# 삼각형과 세 변

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    value = max(a, b, c)
    total = a + b + c
    
    if value >= total - value:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and a != c and b != c:
        print("Scalene")
    elif a == b or a == c or b == c:
        print("Isosceles")