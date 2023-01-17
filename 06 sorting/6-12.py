# 두 배열의 원소 교체

n, k = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

for i in range(k):
    if listA[i] < listB[i]:
        listA[i], listB[i]  = listB[i], listA[i]
    else:
        break

print(sum(listA))