# 1157.py
# 단어 공부

word = input().upper()
word_list = list(set(word))

result = []

for letter in word_list:
    result.append(word.count(letter))

if result.count(max(result)) >= 2:
    print('?')
else:
    print(word_list[result.index(max(result))])