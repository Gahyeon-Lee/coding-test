# 1759.py
# 암호 만들기

l, c = map(int, input().split())
letter = sorted(list(map(str, input().split())))

vowel = ['a', 'e', 'i', 'o', 'u']
s = []

def dfs(n):
    if len(s) == l:
        v, co = 0, 0
        for i in s:
            if i in vowel:
                v += 1
            else:
                co += 1
                
        if v >= 1 and co >= 2:
            print(''.join(s))
        return
    
    for i in range(n, c):
        if letter[i] not in s:
            s.append(letter[i])
            dfs(i + 1)
            s.pop()
            
dfs(0)