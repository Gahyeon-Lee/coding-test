# 1157.py
# 단어 공부

import collections

string = input()

most = collections.Counter(string.upper())
answer = []

max_value = max(list(most.values()))
for key in list(most.keys()):
    if most[key] == max_value:
        answer.append(key)

if len(answer) > 1:
    print("?")
else:
    print(answer[0])
    

# --------------------다른 사람의 풀이----------------------

# set을 이용하여 더욱 간편하게 품
word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:  # set을 사용함에도 불고하고 개수를 쉴 수 있나봄
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])