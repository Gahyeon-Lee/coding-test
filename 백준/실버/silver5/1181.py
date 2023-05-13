# 1181.py
# 단어 정렬

n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)

words = list(set(words))

words.sort()
words.sort(key=len)

for i in words:
    print(i)