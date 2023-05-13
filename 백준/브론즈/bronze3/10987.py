# 10987.py
# 모음의 개수

s = input()
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in s:
    if i in vowel:
        count += 1

print(count)