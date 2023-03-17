# 브루트 포스 알고리즘

def brute_force(target, pattern):
    i, j = 0, 0  # i는 target, j는 pattern의 인덱스
    while i < len(target) and j < len(pattern):
        if target[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == len(pattern):
        return i - len(pattern)
    else:
        return -1

target = "Hello Python World" 
pattern = "Python"
print(brute_force(target, pattern))