# 럭키 스트레이트
# 난이도: 1 | 풀이시간: 20분 | 시간 제한: 1초 | 메모리 제한: 256MB

num = input()
left = num[:len(num) // 2]
right = num[len(num) //2 :]

left_sum = 0
right_sum = 0

for i in left:
    left_sum += int(i)
    
for j in right:
    right_sum += int(j)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
    

# 해설지는 이런 식으로 작성하였다. 놀랍군.
# 하지만 문자열의 길이를 반으로 줄여야 한다는 것은 통했다.
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -=  int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")