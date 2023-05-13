# 4673.py
# 셀프 넘버

nums = list(range(1, 10001))
remove_list = []

sumOf = 0
for num in nums:
    for j in str(num):
        num += int(j)
    if num <= 10000:
        remove_list.append(num)

for i in set(remove_list):
    nums.remove(i)

for i in nums:
    print(i)