# 명령 프롬프트

n = int(input())

first_file = list(input())

for i in range(n - 1):
    other_files = list(input())
    for j in range(len(first_file)):
        if first_file[j] != other_files[j]:
            first_file[j] = '?'

for i in first_file:
    print(i, end='')