# 알파벳 개수
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

count = [0] * 26
s = input()

for i in s:
    count[ord(i) - 97] += 1

for i in count:
    print(i, end=' ')