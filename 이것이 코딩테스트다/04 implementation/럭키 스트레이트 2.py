# 럭키 스트레이트 두 번째 다시 풀어보기

n = input()

f_sum = 0
for i in range(len(n) // 2):
    f_sum += int(n[i])

r_sum = 0
for i in range(len(n) // 2, len(n)):
    r_sum += int(n[i])
    
if f_sum == r_sum:
    print("LUCKY")
else:
    print("READY")