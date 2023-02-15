# 15829.py
# Hashing

n = int(input())
s = input()

hash_sum = 0
for i in range(n):
    hash_sum += ((ord(s[i])-96) * (31 ** i))
print(hash_sum % 1234567891)