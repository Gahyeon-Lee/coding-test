# 5597.py
# 과제 안 내신 분..?

students = [0] * 31

for _ in range(28):
    n = int(input())
    students[n] = 1

for i in range(1, 31):
    if students[i] == 0:
        print(i)