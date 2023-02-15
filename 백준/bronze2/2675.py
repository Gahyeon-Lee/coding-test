# 2675.py
# 문자열의 반복

t = int(input())
 
for _ in range(t):
    new_word = " "
    n, s = input().split()
    for i in s:
        new_word += i * int(n)
    print(new_word.strip())