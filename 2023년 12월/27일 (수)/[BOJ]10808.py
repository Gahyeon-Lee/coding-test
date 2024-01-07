# 10808.py
# 알파벳 개수

s = input()
alphabet = [0] * 26

for i in s:
    alphabet[ord(i) - 97] += 1

for i in alphabet:
    print(i, end=' ')