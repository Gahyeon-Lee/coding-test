# 1316.py
# 그룹 단어 체커

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    
    error = 0
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]
            if new_word.count(word[i]) > 0:
                error += 1
    if error == 0:
        group_word += 1

print(group_word)