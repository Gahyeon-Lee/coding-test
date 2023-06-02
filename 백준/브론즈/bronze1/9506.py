# 9506.py
# 약수들의 합

# join 함수는 str만 할 수 있음
# 리스트는 형 변환 안됨

divisor = []

while True:
    n = int(input())
    
    if n == -1:
        break
    
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    
    if n == sum(divisor):
        print(n, "= " + ' + '.join(map(str, divisor)))
    else:
        print(n, "is NOT perfect.")
    
    divisor.clear()