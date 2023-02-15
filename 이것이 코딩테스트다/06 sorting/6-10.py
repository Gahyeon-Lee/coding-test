# 위에서 아래로

# N을 입력받기
n = int(input())

# N개의 정수를 입력받아 리스트에 저장
nums = []
for _ in range(n):
    nums.append(int(input()))

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
# nums = sorted(nums, reverse=True)

# 리스트 객체의 내장 함수 사용해서 풀음
nums.sort(reverse=True)

# 정렬이 수행된 결과를 출력
for i in nums:
    print(i, end=' ')