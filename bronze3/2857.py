info = []

#자세한 것은 티스토리에 
for _ in range(5):
    info.append(input())
    
flag = 0  #FBI가 포함되어 있는지 확인 없으면 flag는 1로 변하지 않음
for i in range(len(info)):
    if 'FBI' in info[i]:
        print(i+1, end=' ')
        flag = 1
    
if flag == 0:
    print('HE GOT AWAY!')