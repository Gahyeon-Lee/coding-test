# 삼각형 외우기
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
# 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.

"""
    세 각의 크기가 모두 60이면, Equilateral
    세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
    세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
    세 각의 합이 180이 아닌 경우에는 Error
"""

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

total = angle1 + angle2 + angle3

if angle1 == angle2 == angle3:
    print("Equilateral")
elif total == 180 and (angle1 == angle2 or angle1 == angle3 or angle2 == angle3):
    print("Isosceles")
elif total == 180 and angle1 != angle2 != angle3:
    print("Scalene")
else:
    print("Error")