# 효율적인 소수 판별 함수
# N의 약수를 오름차순으로 나열했을 때 가운데 약수를 기준으로 각 등식이 대칭적인 형태를 보임
# 즉 N의 제곱근까지만 확인해봐도 됨

import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))