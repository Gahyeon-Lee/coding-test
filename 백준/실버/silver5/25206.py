# 25206.py
# 너의 평점은

scores = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0
cnt = 0
for i in range(20):
    subject, credit, score = map(str, input().split())
    
    if score != 'P':
        cnt += float(credit)
        total += (float(credit) * scores[score])

print(total / cnt)