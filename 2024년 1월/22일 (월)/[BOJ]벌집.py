# 2292.py
# 벌집

n = int(input())
count = 1
bee_house = 1

while n > bee_house:
    bee_house += count * 6
    count += 1
    
print(count)