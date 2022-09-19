# 검증수
# 첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.
# 첫째 줄에 검증수를 출력한다.

"""
num1, num2, num3, num4, num5 = map(int, input().split())
verification_num = (num1*num1 + num2*num2 + num3*num3 + num4*num4 + num5*num5) % 10
print(verification_num)
"""

# 리팩토링 이후, 위의 풀이보다 4ms 더 빠름
numbers = list(map(int, input().split()))
verification_num = 0

for i in numbers:
    verification_num += i*i

print(verification_num % 10)