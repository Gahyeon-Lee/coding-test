# 13458.py
# 시험 감독

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split()) 

total = n
for people in a:
    people -= b
    
    if people > 0:
        if people % c:
            total += (people // c) + 1
        else:
            total += people // c

print(total)