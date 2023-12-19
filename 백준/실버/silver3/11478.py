# 11478.py
# 서로 다른 부분 문자열의 개수

s = input()

r = set()
for i in range(len(s)):
    for j in range(1, len(s)):
        r.add(s[i:j])

print(r)