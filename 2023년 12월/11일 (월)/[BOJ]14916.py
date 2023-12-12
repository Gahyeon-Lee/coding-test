# 14916.py
# 거스름돈

n = int(input())
count = 0

while True:
    if n % 5 == 0:
        count += n // 5
        break
    else:
        n -= 2
        count += 1
        
    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(count)
    
    
# 가장 큰 단위인 5부터 거슬러 줘야 함
# 문제를 보면 예로 쩍수, 홀수 모두 주어지므로 5의 배수가 될 때까지 2를 뺌
# 그 다음에 5로 나누어 주기만 하면 끝