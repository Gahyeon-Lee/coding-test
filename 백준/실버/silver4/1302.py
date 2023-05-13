# 1302.py
# 베스트셀러

n = int(input())

books = dict()
for _ in range(n):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1
        
max_value = max(books.values())

best = []
for key, value in books.items():
    if value == max_value:
        best.append(key)

best = sorted(best)
print(best[0])