# 7-4.py (보너스)
# 한 출 입력받아 출력하는 소스코드

import sys

# 하나의 문자열 데이터 입력받기
# rstrip() -> 입력 후 엔터가 줄 바꿈 기호로 엽력되는 공백을 제거
input_data = sys.stdin.readline().rstrip()

# 입력받고 문자열 그대로 출력
print(input_data)