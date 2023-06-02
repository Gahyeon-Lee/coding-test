# 10798.py
# 세로읽기

words = []
for _ in range(5):
    word = list(input())
    words.append(word)

for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')