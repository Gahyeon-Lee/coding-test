# 1543.py
# 문서 검색

given = input()
searched = input()

i = 0
count = 0

while i < len(given):
    if given[i:i + len(searched)] == searched:
        i += len(searched)
        count += 1
    else:
        i += 1

print(count)