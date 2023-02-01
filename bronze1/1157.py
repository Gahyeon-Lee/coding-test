# 단어 공부

capital = [0] * 27

string = input()

for i in string.upper():
    num = ord(i) - 65
    capital[num] += 1

