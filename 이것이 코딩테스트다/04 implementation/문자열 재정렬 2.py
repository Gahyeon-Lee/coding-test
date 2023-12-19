# 문자열 재정렬 두 번째 다시 풀어보기

s = input()

alphabet = []
number = []

for i in s:
    if i.isdigit():
        number.append(int(i))
    else:
        alphabet.append(i)
        
alphabet.sort()

print("".join(alphabet), end="")
print(sum(number))