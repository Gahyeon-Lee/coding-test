# 10988.py
# 팰린드롬인지 확인하기

word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)