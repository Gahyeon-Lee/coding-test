# 1406.py
# 에디터

import sys

word = list(input())
m = int(input())
saving = []

for _ in range(m): 
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'P':
        word.append(command[1])
    elif command[0] == 'L' and word:
        saving.append(word.pop())
    elif command[0] == 'D' and saving:
        word.append(saving.pop())
    elif command[0] == 'B' and word:
        word.pop()

answer = word + saving[::-1]
print(''.join(answer))    