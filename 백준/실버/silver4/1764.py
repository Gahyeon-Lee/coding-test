# 1764.py
# 듣보잡

n, m = map(int, input().split())

heard_seen_dict = {}
for _ in range(n + m):
    name = input()
    
    if name not in heard_seen_dict:
        heard_seen_dict[name] = 1
    else:
        heard_seen_dict[name] += 1

named = []
for key, value in heard_seen_dict.items():
    if value == 2:
        named.append(key)
        
print(len(named))

named.sort()
for i in named:
    print(i)

# ------------------------------------ # 
    
n , m = map(int,input().split())
heard = set()
seen = set()

for _ in range(n):
    heard.add(input())
    
for _ in range(m):
    seen.add(input())

arr = sorted(list(heard & seen))
print(len(arr))

for i in arr:
    print(i)