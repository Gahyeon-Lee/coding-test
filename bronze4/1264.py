while 1:
    word = input()
    if word == '#':
        break
    cnt = 0
    for i in word:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)