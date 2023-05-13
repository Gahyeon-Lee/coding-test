# 2941.py
# 크로아티아 알파벳

alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in alpa:
    word = word.replace(i, '*')
print(len(word))