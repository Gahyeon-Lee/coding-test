# 1010.py
# 다리 놓기

import math

t = int(input())

for _ in range(t):
    west, east = map(int, input().split())
    east_f = math.factorial(east)
    west_f = math.factorial(west)
    
    print(east_f // (math.factorial(east - west) * west_f))